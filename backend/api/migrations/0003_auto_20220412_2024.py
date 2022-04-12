# Generated by Django 3.1.3 on 2022-04-12 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220412_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildrenMenusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authName', models.CharField(max_length=20, verbose_name='菜单名称')),
                ('path', models.CharField(max_length=256, verbose_name='菜单地址')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
            ],
            options={
                'verbose_name': '二级菜单',
                'verbose_name_plural': '二级菜单',
                'db_table': 'tb_children_menus',
            },
        ),
        migrations.CreateModel(
            name='ParentMenusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authName', models.CharField(max_length=20, verbose_name='菜单名称')),
                ('path', models.CharField(max_length=256, verbose_name='菜单地址')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('children', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.childrenmenusinfo', verbose_name='二级菜单')),
            ],
            options={
                'verbose_name': '一级菜单',
                'verbose_name_plural': '一级菜单',
                'db_table': 'tb_parents_menus',
            },
        ),
        migrations.DeleteModel(
            name='MenusInfo',
        ),
    ]
