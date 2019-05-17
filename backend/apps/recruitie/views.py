from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CandidateSerializer, LeadSerializer
from .models import Candidate, Lead

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