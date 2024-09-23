from django.urls import path, include

from notes.urls import urlpatterns as notes_urls


app_name = 'api'

urlpatterns = [
]

urlpatterns += notes_urls
