from django.urls import path, include

from notes.urls import urlpatterns as notes_urls


app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += notes_urls
