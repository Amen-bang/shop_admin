from django.urls import path

from api import views

urlpatterns = [
    path('menus/', views.MenusAPIView.as_view()),
]
