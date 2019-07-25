from django.urls import path
from . import views

urlpatterns=[
<<<<<<< HEAD
    path('',views.jkw_center_main,name="jkw_center_main"),
    path('hubungikami/',views.listmasukan, name='halaman_feedback'),
    path('socialmedia/',views.jkw_social_media,name="jkw_social_media"),
=======
<<<<<<< HEAD
    # path('',views.jkw_center_main,name="jkw_center_main")
    path('',views.listmasukan, name='halaman_feedback')
=======
path('',views.jkw_center_main,name="jkw_center_main"),
path('socialmedia',views.jkw_social_media,name="jkw_social_media"),

>>>>>>> 2800f3406266d6710ec34501936b8f22c99c8c17
>>>>>>> 1ae4dbaa872f83fa970d69c6e9ec8d0572159dce
]
