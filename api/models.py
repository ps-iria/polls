from django.db import models

QUESTION = (
    ('текст', 'ответ текстом'),
    ('один вариант', 'ответ с выбором одного варианта'),
    ('несколько вариантов', 'ответ с выбором нескольких вариантов'),
)


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