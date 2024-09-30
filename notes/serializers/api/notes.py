import os
from rest_framework import serializers
from django.conf import settings

from common.serializers.mixins import ExtendedModelSerializer
from notes.models.notes import Notes
from common.utils import markdown_in_file


class NotesListSerializer(ExtendedModelSerializer):
    class Meta:
        model = Notes
        fields = (
            'id',
            'name',
            'created_at',
        )
        read_only_fields = (
            'created_at',
        )


class NotesRetrieveSerializer(ExtendedModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = Notes
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'text',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )

    def get_text(self, obj):
        file_name = f'media/{obj.body.name}'

        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = file.read()
        except (FileNotFoundError, IOError,):
            raise serializers.ValidationError('File does not exist.')
        
        return data
    

class NotesCreateSerializer(ExtendedModelSerializer):
    text = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Notes
        fields = (
            'name',
            'text',
        )
    
    def create(self, validated_data):
        body = validated_data.pop('text')
        validated_data['body'] = markdown_in_file(body)
        
        user = self.context.get('request').user
        validated_data['owner'] = user

        return super().create(validated_data)


class NotesUpdateSerializer(ExtendedModelSerializer):
    text = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Notes
        fields = (
            'name',
            'text',
        )
    
    def update(self, instance, validated_data):
        new_body = validated_data.pop('text', None)
        # Replacing by deleting the old file if there is a new one
        if new_body is not None:
            os.remove(os.path.join(settings.MEDIA_ROOT, instance.body.name))
            new_file = markdown_in_file(new_body, 
                                        instance.body.name.split('/')[-1])
            instance.body = new_file

        return super().update(instance, validated_data)
    