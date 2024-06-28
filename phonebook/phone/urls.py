from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('phn',views.addcont),
    path('disp',views.display),
    path('displ',views.displayname),
    path('del',views.delete),
    path('upd',views.update)
]