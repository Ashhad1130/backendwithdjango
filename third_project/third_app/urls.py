from django.urls import path
from third_app import views

app_name='third_app'
urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('details',views.details,name='details'),
    path('story1',views.story1,name='story1'),
    path('post_detail',views.post_detail,name='post_detail')
]
