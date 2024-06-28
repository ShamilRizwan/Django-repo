from django.urls import path
from .import views
urlpatterns=[
    path('',views.home),
    path('balence',views.bale),
    path('addexpense',views.addexp),
    path('del',views.delete)
]