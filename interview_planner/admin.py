from django.contrib import admin
from .models import Interview


class InterviewAdmin(admin.ModelAdmin):
    list_display = (
        "interviewer",
        "interviewee",
        "start",
        "end",
        "upcoming",
    )

    list_filter = (
        "interviewer",
        "interviewee",
        "start",
        "end",
        "upcoming",
    )


admin.site.register(Interview, InterviewAdmin)