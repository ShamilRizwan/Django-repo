from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('tbl',views.addemp),
    path('disp',views.display),
    path('del',views.delete),
    path('update',views.update)
]