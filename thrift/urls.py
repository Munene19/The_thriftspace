from django.urls import path
from .views import *


urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
