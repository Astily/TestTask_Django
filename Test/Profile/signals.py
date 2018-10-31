from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import DbLog


@receiver(post_save)
def log_change_db(sender, **kwargs):
    log = DbLog(model=sender.__name__, action='EDT')
    log.save()


@receiver(post_delete)
def log_change_db(sender, **kwargs):
    log = DbLog(model=sender.__name__, action='DEL')
    log.save()
