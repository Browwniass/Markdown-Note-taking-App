from common.views.mixins import LCRUDViewSet
from notes.models.notes import Notes
from notes.serializers.api import notes
from drf_spectacular.utils import extend_schema_view, extend_schema



@extend_schema_view(
    list=extend_schema(summary='Список Задач', tags=['Задачи']),
    retrieve=extend_schema(summary='Детально о задаче', tags=['Задачи']),
    create=extend_schema(summary='Создать задачу', tags=['Задачи']),
    update=extend_schema(summary='Изменить задачу', tags=['Задачи']),
    partial_update=extend_schema(summary='Изменить задачу частично', tags=['Задачи']),
    destroy=extend_schema(summary='Удалить задачу', tags=['Задачи']),
)
class NotesModelView(LCRUDViewSet):
    queryset = Notes.objects.all()
    serializer_class = notes.NotesListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return notes.NotesRetrieveSerializer
        elif self.action == 'create':
            return notes.NotesCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return notes.NotesUpdateSerializer
        return self.serializer_class
    



