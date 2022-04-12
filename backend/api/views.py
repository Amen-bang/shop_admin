from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import ParentMenusInfo
from api.serializers import ParentMenusInfoSerializer


# Create your views here.
class MenusAPIView(APIView):
    
    def get(self, request):
        "获取菜单"
        menus = ParentMenusInfo.objects.all()
        ser = ParentMenusInfoSerializer(menus, many=True)
        return Response({"data": ser.data, "meta": {'msg':'获取菜单列表成功', 'status':200}})
