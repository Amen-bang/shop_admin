from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import MyTokenObtainPairSerializer

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomBackend(ModelBackend):
    """
    自定义用户登录，可以使用用户名和手机登录，重写authenticate方法
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class PageNum(PageNumberPagination):
    """
        自定义分页器
    """
    page_size_query_param = 'pagesize'  # 指定每页展示数量的参数
    max_page_size = 10  # 指定每页最大返回量

    # 改写分页器返回参数
    def get_paginated_response(self, data):
        type2role = {
            "1": "普通用户",
            "2": "系统管理员",
            "3": "超级管理员"
            }
        for data_ in data:
            type_ = data_['role']
            role_name = type2role[type_]
            if type_:
                data_['type'] = type_
                data_['role_name'] = role_name
                del(data_['role'])
            # 禁用需要取反和前端保持一致
            data_['is_delete'] = not data_['is_delete']
        return Response(
            {
                'total': self.page.paginator.count,
                "pagenum": self.page.number,  # "页码",
                'users': data,
                'meta': {'msg':'获取成功', 'status':200}
            }
        )
