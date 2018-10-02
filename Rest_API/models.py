from django.db import models


class Lesson(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='Untitled')
    bpm = models.DecimalField(max_digits=5, decimal_places=2, default=120.00)
    notes = models.TextField()

    class Meta:
        ordering = ('created',)