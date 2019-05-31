from rest_framework import serializers

# from .models import Candidate, Lead
from .models import * 

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'first_name', 'last_name', 'location', 'years_of_exp']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'title', 'desc', 'location']

class CandidateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateNote
        fields = ['id', 'user', 'candidate', 'note', 'date']

class LeadNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadNote
        fields = ['id', 'user', 'lead', 'note', 'date']
