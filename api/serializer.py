from rest_framework import serializers
from core.models import SpecialTechnique, SpecialTechniqueCategory, Factory, SpecialTechniqueApplication, \
    FactoryApplication, ServiceCenterRequest, Contact

class SpecialTechniqueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialTechniqueCategory
        fields = [
            'id',
            "name",
            "image"
        ]


class SpecialTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialTechnique
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"


class SpecialTechniqueApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialTechniqueApplication
        fields = "__all__"


class FactoryApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryApplication
        fields = "__all__"


class ServiceCenterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenterRequest
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

