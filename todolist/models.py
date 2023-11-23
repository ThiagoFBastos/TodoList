from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Topico(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    deadline = models.DateField(default = timezone.now)
    start = models.DateField(auto_now_add = True)
    updatedAt = models.DateField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status_choices = [
        ("completed", "completed"),
        ("ongoing", "ongoing"),
        ("canceled", "canceled")
    ]
    status = models.CharField(choices=status_choices, default="ongoing", max_length=50)
    def __str__(self):
        return self.name