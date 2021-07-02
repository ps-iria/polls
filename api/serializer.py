import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from api.models import Poll, Question, Choice, Answer, Vote, QUESTION, \
    PollQuestion


class PKField(serializers.PrimaryKeyRelatedField):

    def to_internal_value(self, data):
        try:
            value = self.get_queryset().get(pk=data)
            return value.id
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ('id',)


class QuestionsSerializer(serializers.ModelSerializer):
    question = serializers.ChoiceField(
        choices=QUESTION, default='ответ текстом'
    )
    choices = ChoiceSerializer(many=True, required=False)
    choices_id = PKField(queryset=Choice.objects.all(), write_only=True)

    class Meta:
        fields = '__all__'
        model = Question


class PollsSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    # questions = QuestionsSerializer(many=True, )
    # questions = PKField(queryset=Question.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'view' in self.context and self.context['view'].action in ['update',
                                                                      'partial_update']:
            self.fields.pop('start_date', None)

    class Meta:
        fields = '__all__'
        model = Poll


class AnswersSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    choice = ChoiceSerializer(read_only=True)
    choice_id = PKField(queryset=Choice.objects.all(),)

    question = QuestionsSerializer(read_only=True)
    question_id = PKField(queryset=Question.objects.all(),
                          write_only=True)

    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('id',)


class VotesSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True, read_only=True)
    poll = PollsSerializer(read_only=True)
    poll_id = PKField(
        queryset=Poll.objects.filter(end_date__gte=datetime.date.today()),
        write_only=True
    )

    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('id', 'user', 'date')

    def create(self, validated_data):
        answers = validated_data.pop('answers', [])
        instance = Vote.objects.create(**validated_data)
        Answer.objects.bulk_create([
            Answer(vote=instance, **a) for a in answers
        ])
        return instance
