from django.contrib import admin
from django.urls import path, include
from jsonPlace_api import urls as json_urls
from jsonPlace_api.views import IndexView;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('json/', include(json_urls)),
    path('', IndexView.as_view(), name='index'),
]