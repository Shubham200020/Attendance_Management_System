from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerilizer

# Create your views here.
@api_view(['GET'])
def getUser(request):
    users=User.objects.all()
    serializer = UserSerilizer(users, many=True)
    return Response(serializer.data)
@api_view(['post'])
def createUser(request):
    serizer=UserSerilizer(data=request.data)
    if serizer.is_valid():
        serizer.save()
        return Response(serizer.data,status=status.HTTP_201_CREATED)
    return Response(serizer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['post'])
def deleteUser(request,id):
    
    try:
        #return Response(request.data)
        user=User.objects.get(id=id)
        
        user.delete()
        return Response(request.data,status=status.HTTP_100_CONTINUE)

    except:
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
@api_view(['PUT'])
def updateUser(request,id):
    user=User.objects.get(id=id)
    print(user)
    serializer = UserSerilizer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
