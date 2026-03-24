from django.contrib import admin
from .models import Counties, LandUseRecord, LandUseClass, Subcounties, CropType, CropTypeClass, CropTypeRecord


@admin.register(LandUseRecord)
class LandUseRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'county', 'subcounty', 'level', 'year', 'season', 'total_hectares', 'geoserver_wms_layername']
    list_filter = ['level', 'year', 'season', 'county']
    search_fields = ['county__adm1_name', 'subcounty__adm2_name']
    ordering = ['-id']


@admin.register(LandUseClass)
class LandUseClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'record', 'name', 'hectares', 'percentage']
    list_filter = ['name']
    search_fields = ['record__county__adm1_name', 'record__subcounty__adm2_name']
    ordering = ['-id']


@admin.register(CropTypeRecord)
class CropTypeRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'county', 'subcounty', 'level', 'year', 'season', 'total_hectares']
    list_filter = ['level', 'year', 'season', 'county']
    search_fields = ['county__adm1_name', 'subcounty__adm2_name']
    ordering = ['-id']


@admin.register(CropTypeClass)
class CropTypeClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'record', 'crop_type', 'hectares', 'percentage']
    list_filter = ['crop_type']
    search_fields = ['record__county__adm1_name']
    ordering = ['-id']


@admin.register(CropType)
class CropTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['name']


@admin.register(Subcounties)
class SubcountiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'adm2_name', 'adm1_name', 'adm2_pcode', 'adm1_pcode']
    search_fields = ['adm2_name', 'adm1_name']


@admin.register(Counties)
class CountiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'adm1_name', 'adm1_pcode']
    search_fields = ['adm1_name']