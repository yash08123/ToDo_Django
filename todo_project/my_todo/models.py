from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    completed = models.BooleanField(default=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['user', 'completed']),
            models.Index(fields=['user', 'created_date']),
        ]
