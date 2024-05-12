import uuid
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

class Note(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

@receiver(pre_save, sender=Note)
def update_note_updated(sender, instance, **kwargs):
    instance.updated = timezone.now()
