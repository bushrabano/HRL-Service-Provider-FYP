from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from pathlib import Path

urlpatterns = [
    path(
        'frontend/<path:path>',
        serve,
        {
            'document_root': Path(__file__).resolve().parent.parent.parent / 'frontend'
        }
    ),

    path('admin/', admin.site.urls),

    path(
        "provider/",
        include("providers.urls")
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)