from rest_framework import serializers

from api.models import Poll


class PollsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Poll
