from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from core.models import SpecialTechnique, SpecialTechniqueCategory, Factory, FactoryApplication
from .serializer import SpecialTechniqueSerializer, SpecialTechniqueCategorySerializer, FactorySerializer, \
    ContactSerializer, FactoryApplicationSerializer
from config.responses import ResponseSuccess, ResponseFail
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


class STAPIView(APIView):
    def get_object(self, id):
        try:
            return SpecialTechnique.objects.get(id=id)
        except SpecialTechnique.DoesNotExist:
            return None

    def get(self, request, id=None):
        if id:
            query = self.get_object(id)
            if query:
                serializer = SpecialTechniqueSerializer(query, many=False)
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("object", status=404)
        queryset = SpecialTechnique.objects.order_by('-pk')
        serializer = SpecialTechniqueSerializer(queryset, many=True)
        return ResponseSuccess(serializer.data)


class STGenericAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin):
    serializer_class = SpecialTechniqueSerializer
    queryset = SpecialTechnique.objects.order_by("-id")
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)


class STCAPIView(APIView):
    def get_object(self, id):
        try:
            return SpecialTechniqueCategory.objects.get(id=id)
        except SpecialTechniqueCategory.DoesNotExist:
            return None

    def get(self, request, id=None):
        if id:
            query = self.get_object(id)
            if query:
                serializer = SpecialTechniqueCategorySerializer(query, many=False)
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("object", status=404)
        queryset = SpecialTechniqueCategory.objects.order_by('top')
        serializer = SpecialTechniqueCategorySerializer(queryset, many=True)
        return ResponseSuccess(serializer.data)


class FactoryAPIView(APIView):
    def get_object(self, id):
        try:
            return Factory.objects.get(id=id)
        except Factory.DoesNotExist:
            return None

    def get(self, request, id=None):
        if id:
            query = self.get_object(id)
            if query:
                serializer = FactorySerializer(query, many=False)
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("object", status=404)
        queryset = Factory.objects.order_by('-pk')
        serializer = FactorySerializer(queryset, many=True)
        return ResponseSuccess(serializer.data)


class FactoryApplicationAPIView(APIView):
    def get_object(self, id):
        try:
            return FactoryApplication.objects.get(id=id)
        except FactoryApplication.DoesNotExist:
            return None

    def get(self, request, id=None):
        if id:
            query = self.get_object(id)
            if query:
                serializer = FactoryApplicationSerializer(query, many=False)
                return ResponseSuccess(serializer.data)
            else:
                return ResponseFail("object", status=404)
        queryset = FactoryApplication.objects.order_by('-pk')
        serializer = FactoryApplicationSerializer(queryset, many=True)
        return ResponseSuccess(serializer.data)


class ContactCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
