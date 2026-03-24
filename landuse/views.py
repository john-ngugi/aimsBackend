from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LandUseRecord, CropTypeRecord
from .serializers import LandUseRecordSerializer, CropTypeRecordSerializer


class LandUseDataView(APIView):
    """
    GET /api/landuse/?county=Murang'a&year=2022&level=county&season=long_rains
    All params are optional - returns all records if none provided
    """
    def get(self, request):
        queryset = LandUseRecord.objects.prefetch_related('classes').all()

        county = request.query_params.get('county')
        subcounty = request.query_params.get('subcounty')
        year = request.query_params.get('year')
        season = request.query_params.get('season')
        level = request.query_params.get('level')

        if county:
            queryset = queryset.filter(county__adm1_name__icontains=county)
        if subcounty:
            queryset = queryset.filter(subcounty__adm2_name__icontains=subcounty)
        if year:
            queryset = queryset.filter(year=year)
        if season:
            queryset = queryset.filter(season=season)
        if level:
            queryset = queryset.filter(level=level)

        serializer = LandUseRecordSerializer(queryset, many=True)
        return Response(serializer.data)


class CropTypeDataView(APIView):
    """
    GET /api/croptype/?county=Murang'a&year=2022&level=county&season=long_rains
    All params are optional
    """
    def get(self, request):
        queryset = CropTypeRecord.objects.prefetch_related(
            'classes', 'classes__crop_type'
        ).all()

        county = request.query_params.get('county')
        subcounty = request.query_params.get('subcounty')
        year = request.query_params.get('year')
        season = request.query_params.get('season')
        level = request.query_params.get('level')

        if county:
            queryset = queryset.filter(county__adm1_name__icontains=county)
        if subcounty:
            queryset = queryset.filter(subcounty__adm2_name__icontains=subcounty)
        if year:
            queryset = queryset.filter(year=year)
        if season:
            queryset = queryset.filter(season=season)
        if level:
            queryset = queryset.filter(level=level)

        serializer = CropTypeRecordSerializer(queryset, many=True)
        return Response(serializer.data)


class WMSLayersView(APIView):
    """
    GET /api/wms-layers/
    Returns all available WMS layers organized by category
    """
    def get(self, request):
        layers = {
            "layer_configs": {
                "landuse": {
                    2022: {"wmsLayer": "Counties:msai4g_lulc_muranga_aoi_final", "name": "Land Use LULC 2022"},
                    2024: {"wmsLayer": "Counties:LULC_MJF1", "name": "Land Use LULC 2024"},
                    2025: {"wmsLayer": "KSA_Rasters:muranga_classification_2025_final", "name": "Land Use LULC 2025"},
                },
                "croptype": {
                    2024: {"wmsLayer": "Counties:Crop classificatio Raster", "name": "Crop Classification"},
                },
            },
            "categories": {
                "Land Cover": {
                    "Land Use LULC": "Counties:msai4g_lulc_muranga_aoi_final",
                    "Muranga LULC 2024": "Counties:LULC_MJF1",
                    "Crop Classification": "Counties:Crop classificatio Raster",
                },
                "Vegetation Indices": {
                    "NDVI Analysis": "Counties:NDVI",
                    "NDWI Analysis": "Agriculture:NDWI_Muranaga_2024",
                    "GNDVI Analysis": "Counties:GNDVI",
                    "GCI Analysis": "Counties:GCI",
                },
                "Topographic": {
                    "Elevation Model": "Counties:Elevation_Muranga",
                    "Slope Analysis": "Counties:SlopeMuranga",
                    "Aspect Analysis": "Counties:aspectMuranga",
                },
                "Climate": {
                    "Rainfall Analysis": "Counties:AnnualRainfall_2024Muranga",
                },
            }
        }
        return Response(layers)


class AvailableYearsView(APIView):
    """
    GET /api/available-years/?type=landuse
    Returns available years for landuse or croptype
    """
    def get(self, request):
        data_type = request.query_params.get('type', 'landuse')

        if data_type == 'croptype':
            years = CropTypeRecord.objects.values_list('year', flat=True).distinct().order_by('year')
        else:
            years = LandUseRecord.objects.values_list('year', flat=True).distinct().order_by('year')

        return Response({'years': list(years)})