from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Optional field
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp for when created
    updated_at = models.DateTimeField(auto_now=True)         # Timestamp auto-updated on save

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Order by newest first
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
