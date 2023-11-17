from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Topico(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    deadline = models.DateField(default = timezone.now)
    start = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name