# Third-party libraries
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView

from .mixins import *

class JsonHeaderView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_json_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_json_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_json_serializer_class(self):
        assert self.json_serializer_class is not None, (
            "'%s' should either include a `json_serializer_class` attribute, "
            "or override the `get_json_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.json_serializer_class

    def get_header_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_header_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_header_serializer_class(self):
        assert self.header_serializer_class is not None, (
            "'%s' should either include a `header_serializer_class` attribute, "
            "or override the `get_header_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.header_serializer_class


class CreateCustomView(CreateSingleModelMixin, JsonHeaderView):
    """
    Concrete view for creating a model instance.
    """
    pass


class CreateLevelView(CreateMultipleModelMixin, JsonHeaderView):
    def get_serializer(self, key, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class(key)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self, key):
        serializer = key + '_serializer_class'
        assert hasattr(self, serializer), (
            "'%s' should either include a `LevelName_serializer_class` attribute, "
            "or override the `get_json_serializer_class()` method."
            % self.__class__.__name__
        )
        serializer = getattr(self, serializer)
        return serializer
