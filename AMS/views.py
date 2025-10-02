from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerilizer,AttendanceSerializer,CourseSerializer,ClassScedule
from .models import USERS,Attendance,Course,ClassScedule
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@api_view(['POST'])
def userSave(request):
    serizer = UserSerilizer(data=request.data)
    if serizer.is_valid():
        serizer.save()
        return Response(serizer.data, status=status.HTTP_201_CREATED)
    return Response(serizer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def userList(responce):
    user=USERS.objects.all()
    serilize=UserSerilizer(user,many=True)
    return Response(serilize.data,status=status.HTTP_200_OK)


@api_view(['GET','PUT','DELETE'])
def userApi(request,id):
    try:
        user=USERS.objects.get(id=id)
    except:
        return Response(request.errors,status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
    if request.method=='GET':
        serilize=UserSerilizer(user)
        return Response(serilize.data)
    elif request.method=='PUT':
        serilize=UserSerilizer(instance=user,data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.data,status=status.HTTP_202_ACCEPTED)
        return Response(serilize.errors,status=status.HTTP_501_NOT_IMPLEMENTED)
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST','GET'])
def course(request):
    serilize=CourseSerializer(data=request.data)
    if  request.method=='POST':
       if serilize.is_valid():
            serilize.save()
            return Response(serilize.data,status=status.HTTP_201_CREATED)
       else:
           return Response(serilize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='GET':
        course=Course.objects.all()
        serilize=CourseSerializer(course,many=True)
        return Response(serilize.data,status=status.HTTP_200_OK)
    
    else:
        return Response(serilize.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE','GET'])
def courseApi(request,id):
    try:
        course=Course.objects.get(id=id)
    except:
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
    if request.method=='PUT':
        serilize=UserSerilizer(instance=course,data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.data,status=status.HTTP_202_ACCEPTED)
        return Response(serilize.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        course.delete()
        return Response(status=status.HTTP_200_OK)
          