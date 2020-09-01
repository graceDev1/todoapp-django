from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now=True)
