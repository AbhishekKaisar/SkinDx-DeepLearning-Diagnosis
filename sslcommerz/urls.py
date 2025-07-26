from django.urls import path
from . import views

urlpatterns = [
    path('success/', views.payment_success, name='payment_success'),
    path('fail/', views.payment_fail, name='payment_fail'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]