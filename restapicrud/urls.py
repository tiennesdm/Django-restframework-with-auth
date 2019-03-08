from django.urls import path

from . import views

urlpatterns = [
     path('', views.CrudRestApiList.as_view()),
    path('create/', views.CrudRestApiCreateList.as_view()),
     path('<int:pk>/', views.CrudRestApiDetail.as_view()),

]
