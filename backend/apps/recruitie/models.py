from django.db import models

# Create your models here.
class Candidate(models.Model):
    first_name = models.CharField(max_length=24, blank=True, null=True)
    last_name = models.CharField(max_length=24, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    years_of_exp = models.IntegerField()


class Lead(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(max_length=50)
    location = models.CharField(max_length=64, blank=True, null=True)
