from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ['completed']

    def __str__(self):
        return self.title

