import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

QUESTION = (
    ('текст', 'ответ текстом'),
    ('один вариант', 'ответ с выбором одного варианта'),
    ('несколько вариантов', 'ответ с выбором нескольких вариантов'),
)


class Choice(models.Model):
    question = models.ForeignKey(
        'Question', related_name='choices', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=64, )


class Poll(models.Model):
    """Атрибуты опроса: название, дата старта, дата окончания, описание."""
    title = models.CharField(max_length=16)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(
        'Question',
        through='PollQuestion',
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    """ Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом,
    ответ с выбором одного варианта, ответ с выбором нескольких вариантов)"""
    text = models.CharField(max_length=255)
    question = models.CharField(
        max_length=50,
        choices=QUESTION,
        default='ответ текстом'
    )

    def __str__(self):
        return self.text


class PollQuestion(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="polls",
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="questions",
    )


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True)
    date = models.DateField(default=datetime.date.today(), editable=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, related_name='answers',
                             on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    value = models.CharField(max_length=128, blank=True, null=True)
