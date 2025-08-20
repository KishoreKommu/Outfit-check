from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Outfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='outfits/')
    description = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    feedback = models.TextField()
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.description}"
