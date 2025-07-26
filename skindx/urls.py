from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Allauth handles Google login, logout, etc.
    path('accounts/', include('allauth.urls')),

    # Custom login and homepage
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),

    # App-specific routes
    path('', include('core.urls')),
    path('payment/', include('sslcommerz.urls')),
]