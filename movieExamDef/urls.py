from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movieExamDef.main.urls')),
    #path('accounts/', include('movieExamDef.accounts.urls'))
]
