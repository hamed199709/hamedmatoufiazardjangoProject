from . import views
from django.urls import path
app_name='comments'
urlpatterns = [
    path('', views.user_comment, name='comments'),
    ]