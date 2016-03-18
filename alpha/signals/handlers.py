from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ..models import Answer

@receiver(post_save, sender=Answer)
def add_ans_count(instance, created, **kwargs):
    if created:
        instance.ques.answers += 1
        instance.ques.save()

@receiver(post_delete, sender=Answer)
def rem_ans_count(instance, **kwargs):
    instance.ques.answers -= 1
    instance.ques.save()
