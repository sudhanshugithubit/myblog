from os import stat
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
from django.contrib import admin

 

urlpatterns = [
    path('', include('homeapp.urls')),
    path('api/', include('homeapp.urls_api')),

    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
#
]

 