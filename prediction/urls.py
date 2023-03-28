from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    
    path('', views.home, name='home'),
    path('predict/', views.predict, name='prediction-form'),
    path('predict/result/', views.result, name='result-page'),
    path('predict/result/diet/', views.diet, name='diet-page'),
    path('predict/result/diet/diet_details', views.diet_details, name='diet-details-page'),
    path('predict/result/diet/diet_details/diet_chart', views.diet_chart, name='diet-chart'),

]