from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # 添加需要token的个人信息
        token['name'] = user.username
        return token

    def validate(self, attrs):
        """
        登录返回token和refresh
        :param attrs:
        :return:
        """
        return_data = {}
        data = super().validate(attrs)
        data['username'] = str(attrs["username"])
        data['token'] = str(data["access"])
        del(data["refresh"])
        del(data["access"])
        return_data['data'] = data
        return_data['meta'] = {'msg':'登录成功', 'status':200}
        return return_data

