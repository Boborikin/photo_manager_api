from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RetrievePhotoSerializer, ListPhotoSerializer, CreatePhotoSerializer
from .models import Photo
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CustomPhotoFilter
from rest_framework.filters import OrderingFilter



class PhotoViewSet(viewsets.GenericViewSet):
    action_serializers = {
        'list': ListPhotoSerializer,
        'retrieve': RetrievePhotoSerializer,
        'create': CreatePhotoSerializer,
    }
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = CustomPhotoFilter
    ordering_fields = ('upload_date',)

    def list(self, request, *args, **kwargs):
        queryset = Photo.objects.filter(user=self.request.user)
        filtered_queryset = self.filter_queryset(queryset)
        serializer = ListPhotoSerializer(filtered_queryset, context={"request": self.request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Photo.objects.filter(user=self.request.user)
        photo = get_object_or_404(queryset, pk=pk)
        serializer = RetrievePhotoSerializer(photo, context={"request": self.request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        self.get_serializer_class()
        print(request.data)
        serializer = CreatePhotoSerializer(data=request.data, context={"request": self.request})
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(PhotoViewSet, self).get_serializer_class()


