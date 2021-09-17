from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import student
from .serializers import studentserializer
# Create your views here.
class studentdata(APIView):

    def get(self,request):
        student1=student.objects.all()
        serializer=studentserializer(student1,many=True)
        return Response(serializer.data)
    def post(self):
    