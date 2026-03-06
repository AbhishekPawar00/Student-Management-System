from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.student_list,name='student_list'),
    path('add/',views.student_add,name='student_add'),
    path('edit/<int:id>/',views.student_edit,name='student_edit'),
    path('delete/<int:id>/',views.student_delete,name='student_delete'),
]
