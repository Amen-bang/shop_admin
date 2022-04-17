from django.urls import path, re_path

from users import views

urlpatterns = [
    path('user/', views.UsersAPIView.as_view()),
    re_path('user/(?P<pk1>\d+)/state/(?P<pk2>\w+)', views.UserStateAPIView.as_view()),
    re_path('user/(?P<pk>\d+)', views.UserAPIView.as_view()),
]
