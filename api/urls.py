from django.urls import path
from .views import getUser,createUser,deleteUser,updateUser
app_name = 'api'
urlpatterns = [
    path('user/get',getUser,name='getUser'),
    path('user/save',createUser,name='createUser'),
    path('user/delete/<str:id>/',deleteUser,name='deleteUser'),
    path('user/update/<str:id>/',updateUser,name='updateUser')
   
]
