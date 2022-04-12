from rest_framework import serializers

from api.models import ChildrenMenusInfo, ParentMenusInfo


class ChildrenMenusInfoializer(serializers.ModelSerializer):
    """二级菜单序列化器"""
    
    class Meta:
        model = ChildrenMenusInfo
        fields = ('id','authName','path')


class ParentMenusInfoSerializer(serializers.ModelSerializer):
    """一级菜单序列化器"""
    # 将二级菜单嵌套序列
    children = ChildrenMenusInfoializer(many=True)

    class Meta:
        model = ParentMenusInfo
        # fields = '__all__'
        fields = ('id','authName','path','children')

