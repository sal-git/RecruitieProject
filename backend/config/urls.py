from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout

from django.conf.urls import include
from rest_framework_simplejwt import views as jwt_views

from config.api import api


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),

    path('api/', include(api.urls)),
    # path('candidates/', include()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Auth
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
