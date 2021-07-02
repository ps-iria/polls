from django.contrib import admin

from api.models import Poll, Question, PollQuestion


class PollQuestionInline(admin.TabularInline):
    model = PollQuestion
    extra = 1


class PollsAdmin(admin.ModelAdmin):
    inlines = [PollQuestionInline, ]
    list_display = (
        'pk',
        'title',
        'start_date',
        'end_date',
        'description'
    )
    search_fields = (
        'title',
    )


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'question',
    )
    search_fields = (
        'title',
    )


admin.site.register(Poll, PollsAdmin)
admin.site.register(Question, QuestionAdmin)
