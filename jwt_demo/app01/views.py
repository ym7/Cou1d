from django.shortcuts import render
from rest_framework.views import APIView
from app01 import models
from rest_framework.response import Response
from autho.authenic import AuthThrough
from utils.maketoken import create_token

# Create your views here.
class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user_obj = User.objects.filter(username=username,password=password).first()
        if user_obj:
            token = create_token({'user_id': user_obj.id,'username': user_obj.username})
            return Response({"code":1000,"msg":token})
        return Response({"code":1001,'msg':'用户名或密码错误'})


class OrderView(APIView):
    authentication_classes = [AuthThrough,]
    def get(self,request,*args,**kwargs):
        return Response("订单列表")




