from rest_framework import serializers
from .models import (
    LandUseRecord, LandUseClass,
    CropTypeRecord, CropTypeClass, CropType
)


class LandUseClassSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()

    class Meta:
        model = LandUseClass
        fields = ['name', 'hectares', 'percentage', 'color']

    def get_color(self, obj):
        return obj.color


class LandUseRecordSerializer(serializers.ModelSerializer):
    classes = LandUseClassSerializer(many=True, read_only=True)
    area_name = serializers.SerializerMethodField()
    wms_layer = serializers.SerializerMethodField()

    class Meta:
        model = LandUseRecord
        fields = ['id', 'area_name', 'level', 'year', 'season', 'total_hectares', 'wms_layer', 'classes']

    def get_area_name(self, obj):
        if obj.subcounty:
            return obj.subcounty.adm2_name
        if obj.county:
            return obj.county.adm1_name
        return None

    def get_wms_layer(self, obj):
        return obj.geoserver_wms_layername


class CropTypeClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='crop_type.name')
    color = serializers.SerializerMethodField()

    class Meta:
        model = CropTypeClass
        fields = ['name', 'hectares', 'percentage', 'color']

    def get_color(self, obj):
        return obj.color


class CropTypeRecordSerializer(serializers.ModelSerializer):
    classes = CropTypeClassSerializer(many=True, read_only=True)
    area_name = serializers.SerializerMethodField()
    wms_layer = serializers.SerializerMethodField()

    class Meta:
        model = CropTypeRecord
        fields = ['id', 'area_name', 'level', 'year', 'season', 'total_hectares', 'wms_layer', 'classes']

    def get_area_name(self, obj):
        if obj.subcounty:
            return obj.subcounty.adm2_name
        if obj.county:
            return obj.county.adm1_name
        return None

    def get_wms_layer(self, obj):
        return obj.geoserver_wms_layername