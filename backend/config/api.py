from rest_framework import routers
from apps.users.views import UserViewSet
from apps.recruitie.views import CandidateViewSet, LeadViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)

# Candidate / Lead API
api.register(r'candidates', CandidateViewSet)
api.register(r'leads', LeadViewSet)
