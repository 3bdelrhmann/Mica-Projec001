from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='home')),

    path('doctors/', include('doctors_app.urls', namespace='doctors')),
    path('labs/', include('labs_app.urls', namespace='labs')),
    path('donation/', include('donation_app.urls', namespace='donation')),
    path('emergency/', include('emergencyPhones_app.urls', namespace='emergency')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
