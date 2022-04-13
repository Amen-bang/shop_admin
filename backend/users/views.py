from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from users.serializers import UserSerializer
from users.utils import PageNum

User = get_user_model()

class UserView(ListCreateAPIView):
    # 指定查询集
    queryset = User.objects.filter(is_staff=False)
    # 指定序列化器
    serializer_class = UserSerializer
    # 指定权限
    permission_classes = [IsAdminUser]
    # 指定分页器
    pagination_class = PageNum

    def get_queryset(self):
        # 默认返回
        # return self.queryset
        # 对前端传递keyword判断返回不同的查询集数据
        # 1、获取keyword数据
        keyword = self.request.query_params.get('keyword')
        # 2、判断keyword
        if keyword is None or keyword == '':
            return User.objects.filter(is_staff=False)
        else:
            return User.objects.filter(username__contains=keyword,is_staff=False)

