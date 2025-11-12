from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path('transaction/', include("apps.transaction.urls")),
    path('directory/', include("apps.directory.urls")),
]
