from django.urls import path
from . import views

urlpatterns=[
<<<<<<< HEAD
    # path('',views.jkw_center_main,name="jkw_center_main")
    path('',views.listmasukan, name='halaman_feedback')
=======
path('',views.jkw_center_main,name="jkw_center_main"),
path('socialmedia',views.jkw_social_media,name="jkw_social_media"),

>>>>>>> 2800f3406266d6710ec34501936b8f22c99c8c17
]
