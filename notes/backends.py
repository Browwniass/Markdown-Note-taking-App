from rest_framework.filters import BaseFilterBackend


class SelfNotes(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)