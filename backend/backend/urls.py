from django.urls import include, path
from users.utils import MyTokenObtainPairView

urlpatterns = [
    # 自定义令牌
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 包含子路由
    path('api/', include('api.urls')),
    path('users/', include('users.urls'))
]
