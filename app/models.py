from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=120)
    message = models.TextField()
    email = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.name



