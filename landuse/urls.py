from django.urls import path
from .views import LandUseDataView, CropTypeDataView, WMSLayersView, AvailableYearsView

urlpatterns = [
    path('landuse/', LandUseDataView.as_view(), name='landuse-data'),
    path('croptype/', CropTypeDataView.as_view(), name='croptype-data'),
    path('wms-layers/', WMSLayersView.as_view(), name='wms-layers'),
    path('available-years/', AvailableYearsView.as_view(), name='available-years'),
]