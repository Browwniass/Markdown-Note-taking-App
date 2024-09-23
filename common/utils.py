import uuid

from django.core.files.base import ContentFile


def markdown_in_file(data, file_name=None):
    if file_name == None: file_name = f'{uuid.uuid4()}.md'
    return ContentFile(data.encode('utf-8'), name=file_name)