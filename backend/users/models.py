from django.contrib.auth.models import AbstractUser
from django.db import models


# 继承AbstractUser
class User(AbstractUser):
    # 使用继承自带的username，password，email
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    role = models.CharField(max_length=6, choices=(
        ("1", "普通用户"), ("2", "系统管理员"), ("3", "超级管理员")), default="1", verbose_name="用户角色")
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
