from django.urls.converters import StringConverter


class CaseInsensitiveConverter(StringConverter):
    regex = '[\w-]+'

    def to_python(self, value):
        return value.lower()

    def to_url(self, value):
        return value
