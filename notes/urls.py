from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notes.views.notes import NotesModelView, GrammarCheck


router = DefaultRouter()

router.register(r'notes', NotesModelView, 'notes')

urlpatterns = [
    path('', include(router.urls)),
    path('grammar/', GrammarCheck.as_view(), name='grammar') 
]
