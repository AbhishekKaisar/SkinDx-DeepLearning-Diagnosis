from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test-skin/', views.test_skin, name='test_skin'),
    path('logout/', views.logout_view, name='logout'),
    path('trial-ends/', views.trial_ends, name='trial_ends'),

]

# Serve uploaded media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
