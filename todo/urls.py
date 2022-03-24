from django.urls import path
from . import views
from .views import TWU

app_name = 'todo'

urlpatterns = [
    path('facewipeWeb/<str:user_id>/<str:access_token>/<str:access_token_secret>/', TWU.as_view(), name='index'),
]
