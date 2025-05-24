from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DailyMealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    breakfast = models.CharField(max_length=255, blank=True)
    lunch = models.CharField(max_length=255, blank=True)
    snacks = models.CharField(max_length=255, blank=True)
    dinner = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date}"