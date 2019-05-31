from rest_framework import routers
from rest_framework.renderers import CoreJSONRenderer
from django.urls import path, include
from . import views

app_name = 'recruitie'
router = routers.DefaultRouter()
# NOTE routes in config/api
# router.register(r'candidatenotes', views.CandidateNoteViewSet, 'candidatenotes')
# router.register(r'leadnotes', views.LeadNoteViewSet, 'leadnotes')
# router.register(r'candidates', views.CandidateViewSet, 'candidates')
# router.register(r'leads', views.LeadViewSet, 'leads')

router.default_schema_renderers = [CoreJSONRenderer]

urlpatterns = [
    path('', include(router.urls))
]
