from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from users.utils import MyTokenObtainPairView

urlpatterns = [
    # 认证令牌
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新令牌
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 自定义令牌
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 包含子路由
    path('', include('api.urls'))
]
