from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('about', views.about, name='about') , 
    path('<int:question_id>/', views.detail, name='details') ,
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),          
               
]