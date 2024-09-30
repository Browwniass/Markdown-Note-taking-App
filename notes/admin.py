from django.contrib import admin

from notes.models.notes import Notes


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'body', 'owner', 'created_at', 'updated_at'
    )
