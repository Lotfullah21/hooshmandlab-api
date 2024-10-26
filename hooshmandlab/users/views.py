from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Student
# Create your views here.


@api_view()
def users_view(request):
    students = Student.objects.all()
    print("Students",students)
    return Response({"message":"Hell world"},status=status.HTTP_200_OK)

class CourseList(APIView):
    def get(self, request):
        return Response({"message":"List of courses"},status=status.HTTP_200_OK)
    
    def post(self, request):
        name = request.data.get("name")
        if name:
            return Response({"message":name+" Enrolled!!!!"}, status=status.HTTP_200_OK)
        return Response({"message":"No name provided"}, status=status.HTTP_200_OK)
    
class Course(APIView):
    def get(self, request,pk):
        return Response({"message":"Book with id = "+str(pk)}, status=status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({"message":request.data.get("name")}, status=status.HTTP_200_OK)