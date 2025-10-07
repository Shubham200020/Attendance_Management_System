from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerilizer,AttendanceSerializer,CourseSerializer,ClassSceduleSerializer
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

@api_view(['GET', 'POST'])
def Classes(request):  
    if request.method == 'GET':    
        classes = ClassScedule.objects.all()     
        serializer = ClassSceduleSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ClassSceduleSerializer(data=request.data)  
        if serializer.is_valid():        
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE','GET'])
def classApi(request,id):
    try:
        classes=ClassScedule.objects.get(id=id)
    except:
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
    
    if request.method=='PUT':
        serilize=ClassSceduleSerializer(instance=classes,data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.date,status=status.HTTP_202_ACCEPTED)
        return Response(serilize.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        classes.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST','GET'])
def attendance(request):
    serilize=AttendanceSerializer(data=request.data)
    if request.method=='POST':
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serilize.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        attendance=Attendance.objects.all()
        serilize=AttendanceSerializer(attendance,many=True)
        return Response(serilize.data,status=status.HTTP_200_OK)
    
@api_view(['POST'])
def login(request):
    email=request.data.get('email')
    password=request.data.get('password')
    try:
        data=USERS.objects.get(email=email)
       
        if data.password==password:
            serialize=UserSerilizer(data)
            return Response(serialize.data,status=status.HTTP_200_OK)
        return Response({'error':'invailed password'})
        

    except(Exception):
        return Response({'error':'Invailid email'})
