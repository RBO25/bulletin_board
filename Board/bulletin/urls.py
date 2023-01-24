from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', BulletinList.as_view()),
    path('<int:pk>', BulletinDetail.as_view(), name='bulletin'),
    path('create/', BulletinCreate.as_view(), name='bulletin_create'),
    path('<int:pk>/update/', BulletinUpdate.as_view(), name='bulletin_update'),
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
]