
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p/', include('mobiles.urls')),
    path('t/', include('tabs.urls')),
]
