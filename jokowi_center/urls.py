from django.urls import path
from . import views

urlpatterns=[
    path('',views.jkw_center_main,name="jkw_center_main"),
    path('hubungikami/',views.listmasukan, name='hubungikami'),
    path('socialmedia/',views.jkw_social_media,name="jkw_social_media"),
    path('<int:blog_id>/',views.blog_detail,name='blog_detail'),
]
