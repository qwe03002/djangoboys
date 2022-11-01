from django.urls import path
# 장고 함수인 path 와 blog 애플리케이션에서 사용할 모든 views를 import함(가져옴)
from . import views # .은 현재 내가있는 위치를 말함

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('list',views.post_list, name='post_list'),
]