from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


class Interview(models.Model):
    interviewer = models.ForeignKey(
        User, related_name='interviewer', on_delete=models.CASCADE
    )
    interviewee = models.ForeignKey(
        User, related_name='interviewee', on_delete=models.CASCADE
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    resume1 = models.FileField(
        blank=True, null=True
    )
    upcoming = models.BooleanField(
        default=True
    )

    def __str__(self):
        return " ".join(map(str, [self.interviewer, self.interviewee, self.start, self.end]))

    class Meta:
        ordering = ['start', 'end']

    def save(self, *args, **kwargs):
        if self.interviewer.id == self.interviewee_id:
            raise ValidationError(_('Interviews should be scheduled between 2 different persons'))

        if self.start > self.end:
            raise ValidationError(_('Start time cannot be greater than end time'))
        
        scheduled_interview_objects = Interview.objects.filter(
            (Q(interviewer_id__in=(self.interviewer.id, self.interviewee.id)) |
            Q(interviewee_id__in=(self.interviewer.id, self.interviewee.id))) &
            ~Q(id=self.id),
            upcoming=True
        )

        for interview in scheduled_interview_objects:
            if self.check_clash(interview):
                raise ValidationError(_('Interviews are clashing.'))

        super().save(*args, **kwargs)  # call the actual save method

    def check_clash(self, interview):
        interview_start = interview.start
        interview_end = interview.end
        if self.start < interview_start < self.end or self.start < interview_end < self.end:
            return True
        if interview_start < self.start < interview_end or interview_start < self.end < interview_end:
            return True
        return False
