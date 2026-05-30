from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accaunt/', include('django.contrib.auth.urls')),
    path('accaunts/', include('accaunts.urls')),
    path('', include('blog.urls')),  # Bu yerda hech qanday ListView import qilinmasligi kerak!
]