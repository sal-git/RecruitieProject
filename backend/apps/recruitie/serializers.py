from rest_framework import serializers

from .models import Candidate, Lead

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'location', 'years_of_exp']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['title', 'desc', 'location']