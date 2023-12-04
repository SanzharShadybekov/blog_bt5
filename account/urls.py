from django.urls import path
from dj_rest_auth.views import LoginView
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.CustomLogoutView.as_view()),
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
]

