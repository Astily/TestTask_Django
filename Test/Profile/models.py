from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

'''
class Profile(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    birth = models.DateField()
    biography = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()


    def __str__(self):
        return self.firstName + ' ' + self.lastName
'''


class LogStore(models.Model):
    executionTime = models.TimeField()
    url = models.CharField(max_length=255)

    def __str__(self):
        return 'Logfile(' + str(self.executionTime) + ', ' + str(self.url) + ')'


class CustomUser(AbstractUser):
    birth = models.DateField(blank=True)
    biography = models.TextField(blank=True)
    emailPublic = models.EmailField(blank=True)

    phone_regex = RegexValidator(regex=r'^\+\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=16, blank=True)

    def __str__(self):
        return self.email


class IpUsers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.ip, self.user, self.time)


class DbLog(models.Model):
    act = (
        ('CRT', 'Created'),
        ('EDT', 'Edited'),
        ('DEL', 'Deleted'),
    )

    model = models.CharField(max_length=50)
    action = models.CharField(max_length=3, choices=act, default='EDT')
    time = models.DateTimeField(auto_now_add=True)
