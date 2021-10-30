from django.urls import path

from wantyourskillapp import views

urlpatterns = [
    path('', views.index)
]
