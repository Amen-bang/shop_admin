from django.contrib.auth import get_user_model
from rest_framework import serializers
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


class UserSerializer(serializers.ModelSerializer):
    """
        用户表序列化器
    """

    class Meta:
        # 指定生成序列化字段的模型类
        model = User
        # 指定字段
        fields = ('id', 'username', 'mobile', 'email', 'role', 'is_delete','password')
        extra_kwargs = {
            "password": {
                'required': False,
                'write_only': True,  # 不参与序列化，只参与反序列化
                'max_length': 20,
                'min_length': 8
            },
            "username": { 
                'required': False,
                'max_length': 20,
                'min_length': 2
            },
            "mobile":{
                'required': False
            }
        }

    # 手机号唯一值判断
    def validate_mobile(self, attrs):
        try:
            user = User.objects.get(mobile=attrs)
        except:
            user = None
        if user and self.context['request']._request.method == 'POST':
            raise serializers.ValidationError('手机号已注册')
        return attrs

    def create(self, validated_data):
        # 重写create方法进行密码加密
        # 直接进行密码加密保存
        user = User.objects.create_user(**validated_data)
        return user
