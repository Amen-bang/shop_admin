import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
# from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer
from users.utils import PageNum

User = get_user_model()

class UsersAPIView(ListCreateAPIView):
    """获取所有的用户,添加用户视图"""
    # 指定查询集
    # queryset = User.objects.filter(is_staff=False)is_staff 过滤掉管理员
    queryset = User.objects.all()
    # 指定序列化器
    serializer_class = UserSerializer
    # 认证策略属性
    # authentication_classes = (TokenAuthentication)
    # 指定权限
    # permission_classes = [IsAdminUser]
    # 指定分页器
    pagination_class = PageNum

    # 重写获取数据集方法，增加搜搜匹配数据
    def get_queryset(self):
        # 默认返回queryset查询集的值
        # return self.queryset

        # 对前端传递keyword判断返回不同的查询集数据
        # 1、获取keyword数据
        keyword = self.request.query_params.get('query')
        print(keyword)
        # 2、判断keyword
        if keyword is None or keyword == '':
            return User.objects.all()
        else:
            # 包含的意思：__contains
            return User.objects.filter(username__contains=keyword)

    def create(self, request, *args, **kwargs):
        # 自定义添加用户返回数据
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return_data = {}
        return_data['data'] = serializer.data
        return_data['meta'] = {'msg':'登录成功', 'status':201}
        return Response(return_data)


class UserAPIView(RetrieveUpdateDestroyAPIView):
    """查找，修改，删除用户视图"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        "查询一个用户数据"
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        "更新一个用户数据"
        return self.update(request, pk)

    def delete(self, request, pk):
        "删除一个用户数据,如果想要逻辑删除使用更新的方式"
        return self.destroy(request, pk)
    

class UserStateAPIView(APIView):
    
    def put(self, request, pk1, pk2):
        """
        修改用户状态
        """
        print(pk1,pk2)
        try:
            user = User.objects.get(id=pk1)
        except:
            raise Response({'未找到相应数据'}, status=400)
        if pk2 == "true":
            user.is_delete = False
        else:
            user.is_delete = True
        user.save()
        return Response({"id": pk1, "status": not user.is_delete})
