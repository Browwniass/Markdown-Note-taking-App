from django_filters import rest_framework as filters
from django.utils.timezone import make_aware
from datetime import datetime, time
from notes.models.notes import Notes


class StartOfDayDateTimeFilter(filters.DateTimeFilter):
    def filter(self, qs, value):
        if value and isinstance(value, datetime) and value.time() == time.min:
            # To filter with the exact operator, you need to search all day (from 00:00 to 23:59)
            if self.lookup_expr == 'exact':
                start_of_day = make_aware(datetime.combine(value.date(), time.min))
                end_of_day = make_aware(datetime.combine(value.date(), time.max))
                return qs.filter(**{
                    f"{self.field_name}__gte": start_of_day,
                    f"{self.field_name}__lte": end_of_day,
                }) 
            else:
                #  For the rest of the filters (gt, lt), we leave only the beginning of the day
                value = make_aware(datetime.combine(value.date(), time.min))
        return super().filter(qs, value)
    

class NotesFilter(filters.FilterSet):
    created_at = StartOfDayDateTimeFilter()
    updated_at = StartOfDayDateTimeFilter()

    class Meta:
        model = Notes
        fields = {
            'created_at': ['exact', 'gt', 'lt'],
            'updated_at': ['exact', 'gt', 'lt'],
        }