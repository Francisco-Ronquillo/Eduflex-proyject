from django.urls import path
from PROFESOR.views import *
app_name = 'profesor'
urlpatterns = [
path('dashboardTeacher/',DashboardTeacher.as_view(),name='dashboardTeacher'),
]