from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('study/', views.study, name="study"),
    path('toprank/', views.toprank, name="toprank")
]