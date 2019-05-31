from django.db import models
from django.conf import settings

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=24, blank=True, null=True)
    last_name = models.CharField(max_length=24, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    years_of_exp = models.IntegerField()

class Lead(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(max_length=50)
    location = models.CharField(max_length=64, blank=True, null=True)

class CandidateNote(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='candidate_user', on_delete=models.CASCADE, default=0)
    candidate = models.ForeignKey(Candidate, related_name='candidate', on_delete=models.CASCADE)
    note = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

class LeadNote(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lead_user', on_delete=models.CASCADE, default=0)
    lead = models.ForeignKey(Lead, related_name='lead', on_delete=models.CASCADE)
    note = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)