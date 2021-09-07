from django.urls import path
from.import views

urlpatterns = [
   path("login/", views.login.as_view(), name="login"),
   path("sigup/", views.register.as_view(), name="sigin"),
    path("logout", views.handlelogout, name="logout"),
    path("", views.home, name="home"),
    path("userdetails", views.AllUserDetail, name="userdetails"),
    path("updateuser/<int:myid>", views.AuthorUpdateView.as_view()),
    path('chat/<str:username>/', views.room, name='room'),
    path('<str:username>', views.oneuserchat, name="chatroom")
    ]