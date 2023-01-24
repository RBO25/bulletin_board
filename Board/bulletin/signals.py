from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers
from .models import *


@receiver(post_save, sender=Bulletin)
def notify_feedback(sender, instance, created, **kwargs):
    subject = f'{instance.author}'

    mail_managers(
        subject=subject,
        message=instance.feedback,
    )


post_save.connect(notify_feedback, sender=Bulletin)