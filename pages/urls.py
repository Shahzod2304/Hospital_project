from django.urls import path 
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('doctor/', Doctor.as_view(), name='doctor'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('treatment/', Treatment.as_view(), name='treatment'),
]



