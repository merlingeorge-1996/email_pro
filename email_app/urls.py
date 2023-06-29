from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.student,name='student'),
    path('student_details',views.student_details,name='student_details'),
    path('sndmail',views.sndmail,name="sndmail"),



]
