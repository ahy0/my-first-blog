from django.contrib import admin
from django.urls import path, include     # django.urls.include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),  # include 대상은 '' 속애!!
]