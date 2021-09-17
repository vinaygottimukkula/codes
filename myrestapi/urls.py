.py so that it can display views.

from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from rest_framework.urlpatterns import format_suffix_patterns
from studentresultanayalasys import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('student/', views.studentdata.as_view()),