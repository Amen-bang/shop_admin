from pickle import FALSE

from django.db import models


# 定义一级菜单目录模型
class ParentMenusInfo(models.Model):
    authName = models.CharField(max_length=20, verbose_name='菜单名称')
    path = models.CharField(max_length=256, verbose_name='菜单地址')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    
    class Meta:
        db_table = 'tb_parents_menus'  # 指明数据库表名
        verbose_name = '一级菜单'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.authName


# 定义二级菜单目录模型
class ChildrenMenusInfo(models.Model):
    authName = models.CharField(max_length=20, verbose_name='菜单名称')
    path = models.CharField(max_length=256, verbose_name='菜单地址')
    parent_id = models.ForeignKey(ParentMenusInfo, on_delete=models.CASCADE, verbose_name='二级菜单',null=FALSE,related_name='children')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    
    class Meta:
        db_table = 'tb_children_menus'  # 指明数据库表名
        verbose_name = '二级菜单'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.authName
