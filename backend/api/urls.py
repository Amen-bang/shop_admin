from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from api import views

urlpatterns = [
    # 认证令牌
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新令牌
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('menus/', views.MenusAPIView.as_view()),
]
