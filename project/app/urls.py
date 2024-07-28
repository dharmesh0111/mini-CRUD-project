
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.index),
    path('insert',views.insertData),
    path('delete/<rid>',views.deletedata),
    path('edit/<rid>',views.updatedata),
]

