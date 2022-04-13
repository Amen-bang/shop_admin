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

    def get_paginated_response(self, data):
        return Response(
            {
                'count': self.page.paginator.count,
                'lists': data,
                "page": self.page.number,  # "页码",
                "pages": self.page.paginator.num_pages,  # "总页数",
                "pagesize": self.max_page_size  # "页容量"
            }
        )
