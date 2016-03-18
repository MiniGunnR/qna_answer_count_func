from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    body = models.TextField()
    answers = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __unicode__(self):
        return self.body

class Answer(models.Model):
    ques = models.ForeignKey('Question')
    body = models.TextField()

    def __unicode__(self):
        return self.body
