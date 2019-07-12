from rest_framework import (mixins, status)
from rest_framework.response import Response

from levels.api.v2.serializers import HeaderCreateSerializer
from levels.models import Header


class CreateSingleModelMixin(mixins.CreateModelMixin):
    """
        Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        json_serializer = self.get_json_serializer(data=request.data)
        json_serializer.is_valid(raise_exception=True)
        data = json_serializer.data['jsonToDb']
        # Check if a header_serializer_class are provided and validate
        header_serializer = self.get_header_serializer(data=data['header'])
        header_serializer.is_valid(raise_exception=True)
        # Check if a game serializer_class are provided and validate
        serializer = self.get_serializer(data=data['levels'])
        serializer.is_valid(raise_exception=True)
        # Creating a Header Instance
        header = self.perform_header_create(header_serializer)
        # Creating a Game or Assesment Instance
        self.perform_create(serializer, header)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer, header):
        serializer.save(header=header)
    
    def perform_header_create(self, serializer):
        serializer.save()
        return serializer.instance


class CreateMultipleModelMixin(mixins.CreateModelMixin):
    """
        Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        json_serializer = self.get_json_serializer(data=request.data)
        json_serializer.is_valid(raise_exception=True)
        data = json_serializer.data['jsonToDb']
        # Check if a header_serializer_class are provided and validate
        header_serializer = self.get_header_serializer(data=data['header'])
        header_serializer.is_valid(raise_exception=True)
        # Check if a game serializer_class are provided and validate
        key = data['header'].get('game_key', None)
        serializer = self.get_serializer(key, data=data['levels'])
        serializer.is_valid(raise_exception=True)
        # Creating a Header Instance
        header = self.perform_header_create(header_serializer)
        # Creating a Game or Assesment Instance
        self.perform_create(serializer, header)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer, header):
        serializer.save(header=header)
    
    def perform_header_create(self, serializer):
        serializer.save()
        return serializer.instance
