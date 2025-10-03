from django.urls import path
from .views import *
app_name='AMS'
urlpatterns = [
    path('user/save',userSave,name='usersave'),
    path('user/list',userList,name='userlist'),
    path('user/manipulate/<str:id>/',userApi,name='userapi'),
    path('course/',course,name='course'),
    path('courseapi/<str:id>/',courseApi,name='courseapi'),
]

