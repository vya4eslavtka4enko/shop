from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('kids_clothes',views.kids_clothes,name='kids_clothes'),
    path('man_clothes',views.man,name='man_clothes'),
    path('woman_clothes',views.woman,name='woman_clothes'),
]