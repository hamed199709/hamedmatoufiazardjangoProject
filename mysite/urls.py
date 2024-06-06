from . import views
from django.urls import path
app_name='mysite'
urlpatterns=[
    path('', views.about_us, name='about_us'),
    path('contact-us', views.contact_us, name='contact_us'),

]