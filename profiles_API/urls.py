from django.urls import path
from profiles_API import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
