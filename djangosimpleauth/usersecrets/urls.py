from django.urls import path
from . import views

app_name = 'usersecrets'

urlpatterns = [
    path('', views.secret, name='secret'),
]
