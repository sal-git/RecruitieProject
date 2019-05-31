from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

# Create your views here.
class CandidateViewSet(viewsets.ModelViewSet):
    model = Candidate
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_queryset(self):
        # TODO get only candidates from requesting user
        return Candidate.objects.all()

class LeadViewSet(viewsets.ModelViewSet):
    model = Lead
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class CandidateNoteViewSet(viewsets.ModelViewSet):
    model = CandidateNote
    queryset = CandidateNote.objects.all()
    serializer_class = CandidateNoteSerializer

class LeadNoteViewSet(viewsets.ModelViewSet):
    model = LeadNote
    queryset = LeadNote.objects.all()
    serializer_class = LeadNoteSerializer
