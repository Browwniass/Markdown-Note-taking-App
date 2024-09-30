from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from common.views.mixins import LCRUDViewSet
from notes.backends import SelfNotes
from notes.models.notes import Notes
from notes.serializers.api import notes
from notes.filters import NotesFilter


@extend_schema_view(
    list=extend_schema(summary='Список Заметок', tags=['Заметки']),
    retrieve=extend_schema(summary='Детально о заметке', tags=['Заметки']),
    create=extend_schema(summary='Создать заметку', tags=['Заметки']),
    update=extend_schema(summary='Изменить заметку', tags=['Заметки']),
    partial_update=extend_schema(summary='Изменить заметку частично', tags=['Заметки']),
    destroy=extend_schema(summary='Удалить заметку', tags=['Заметки']),
)
class NotesModelView(LCRUDViewSet):
    queryset = Notes.objects.all()
    serializer_class = notes.NotesListSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        SelfNotes,
    )
    filterset_class = NotesFilter
    ordering_fields = ('name', 'created_at', 'updated_at',)
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return notes.NotesRetrieveSerializer
        elif self.action == 'create':
            return notes.NotesCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return notes.NotesUpdateSerializer
        return self.serializer_class
    
