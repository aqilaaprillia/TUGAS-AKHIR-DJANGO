from django.utils.translation import gettext_lazy as _
from django.db import models


class Task(models.Model):
    # define status choices/options
    class TaskStatus(models.TextChoices):
        TODO = 'Matematika', _('Matematika')
        IN_PROGRESS = 'Sistem Informasi', _('Sistem Informasi')
        CLOSED = 'Aktuaria', _('Aktuaria')
    
    # define columns
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # define table name
        db_table = 'tasks'