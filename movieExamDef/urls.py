from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movieExamDef.main.urls')),
    path('accounts/', include('movieExamDef.accounts.urls')),
    path('api/', include('movieExamDef.rest_api.urls')),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
