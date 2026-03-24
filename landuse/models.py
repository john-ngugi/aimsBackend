from django.contrib.gis.db import models



# class LandUseModel(models.Model):
#     crop = models.IntegerField()
#     crop_area = models.FloatField(help_text="Area in hectares")
    
#     trees = models.IntegerField()
#     trees_area = models.FloatField(help_text="Area in hectares")
    
#     built_up = models.IntegerField()
#     built_up_area = models.FloatField(help_text="Area in hectares")
    
#     water = models.IntegerField()
#     water_area = models.FloatField(help_text="Area in hectares")
    
#     bareground = models.IntegerField()
#     bareground_area = models.FloatField(help_text="Area in hectares")
    
#     grassland = models.IntegerField()
#     grassland_area = models.FloatField(help_text="Area in hectares")
    
#     year = models.DateField()
#     geoserver_link = models.URLField()

#     # """     def __str__(self):
#     #         return f"LandUse({self.year}) - Crop: {self.crop_area}ha, Trees: {self.trees_area}ha, Built-up: {self.built_up_area}ha" """
    
#     def __str__(self):
#         return f"LandUseModel(crop={self.crop}, trees={self.trees}, built_up={self.built_up}, water={self.water}, bareground={self.bareground}, grassland={self.grassland}, year={self.year}, geoserver_link={self.geoserver_link})"
    
    
class Subcounties(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    adm2_name = models.CharField(max_length=80, blank=True, null=True)
    adm2_name1 = models.CharField(max_length=80, blank=True, null=True)
    adm2_name2 = models.CharField(max_length=80, blank=True, null=True)
    adm2_name3 = models.CharField(max_length=80, blank=True, null=True)
    adm2_pcode = models.CharField(max_length=80, blank=True, null=True)
    adm1_name = models.CharField(max_length=80, blank=True, null=True)
    adm1_name1 = models.CharField(max_length=80, blank=True, null=True)
    adm1_name2 = models.CharField(max_length=80, blank=True, null=True)
    adm1_name3 = models.CharField(max_length=80, blank=True, null=True)
    adm1_pcode = models.CharField(max_length=80, blank=True, null=True)
    adm0_name = models.CharField(max_length=80, blank=True, null=True)
    adm0_name1 = models.CharField(max_length=80, blank=True, null=True)
    adm0_name2 = models.CharField(max_length=80, blank=True, null=True)
    adm0_name3 = models.CharField(max_length=80, blank=True, null=True)
    adm0_pcode = models.CharField(max_length=80, blank=True, null=True)
    valid_on = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    area_sqkm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cod_versio = models.CharField(max_length=80, blank=True, null=True)
    lang = models.CharField(max_length=80, blank=True, null=True)
    lang1 = models.CharField(max_length=80, blank=True, null=True)
    lang2 = models.CharField(max_length=80, blank=True, null=True)
    lang3 = models.CharField(max_length=80, blank=True, null=True)
    adm2_ref_n = models.CharField(max_length=80, blank=True, null=True)
    center_lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    center_lon = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    


    class Meta:
        managed = False
        db_table = 'Subcounties'
        verbose_name = 'Subcounty'
        verbose_name_plural = 'Subcounties'

    def __str__(self):
        return self.adm2_name or self.adm2_ref_n or f"Subcounty {self.pk}"
        
        
class Counties(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    adm1_name = models.CharField(max_length=80, blank=True, null=True)
    adm1_name1 = models.CharField(max_length=80, blank=True, null=True)
    adm1_name2 = models.CharField(max_length=80, blank=True, null=True)
    adm1_name3 = models.CharField(max_length=80, blank=True, null=True)
    adm1_pcode = models.CharField(max_length=80, blank=True, null=True)
    adm0_name = models.CharField(max_length=80, blank=True, null=True)
    adm0_name1 = models.CharField(max_length=80, blank=True, null=True)
    adm0_name2 = models.CharField(max_length=80, blank=True, null=True)
    adm0_name3 = models.CharField(max_length=80, blank=True, null=True)
    adm0_pcode = models.CharField(max_length=80, blank=True, null=True)
    valid_on = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    area_sqkm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cod_versio = models.CharField(max_length=80, blank=True, null=True)
    lang = models.CharField(max_length=80, blank=True, null=True)
    lang1 = models.CharField(max_length=80, blank=True, null=True)
    lang2 = models.CharField(max_length=80, blank=True, null=True)
    lang3 = models.CharField(max_length=80, blank=True, null=True)
    adm1_ref_n = models.CharField(max_length=80, blank=True, null=True)
    center_lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    center_lon = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Counties'
        verbose_name = 'County'
        verbose_name_plural = 'Counties'

    def __str__(self):
        return self.adm1_name or f"County {self.pk}"
        
            
class LandUseRecord(models.Model):
    SEASON_CHOICES = [
        ('long_rains', 'Long Rains'),
        ('short_rains', 'Short Rains'),
    ]
    
    LEVEL_CHOICES = [
        ('county', 'County'),
        ('subcounty', 'Sub-County'),
    ]

    county = models.ForeignKey('Counties', on_delete=models.CASCADE, related_name='landuse_records', null=True, blank=True)
    subcounty = models.ForeignKey('Subcounties', on_delete=models.CASCADE, related_name='landuse_records', null=True, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='subcounty')
    year = models.IntegerField()
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, null=True, blank=True)
    total_hectares = models.FloatField()
    geoserver_wms_layername = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('county', 'subcounty', 'year', 'season')

    def __str__(self):
        area = self.subcounty or self.county
        return f"{area} - {self.year} ({self.get_season_display()})"

    def sync_county_totals(self):
        from django.db.models import Sum

        if self.level != 'subcounty' or not self.subcounty:
            return

        # use pcode instead of name - more reliable
        parent_county = Counties.objects.get(adm1_pcode=self.subcounty.adm1_pcode)
        print(f"Syncing county totals for {parent_county.adm1_name} based on subcounty {self.subcounty.adm2_name}")
        county_record, _ = LandUseRecord.objects.get_or_create(
            county=parent_county,
            subcounty=None,
            level='county',
            year=self.year,
            season=self.season,
            defaults={'total_hectares': 0, 'geoserver_wms_layername': self.geoserver_wms_layername}
        )

        # get all subcounty records for this county/year/season
        subcounty_records = LandUseRecord.objects.filter(
            county=parent_county,
            level='subcounty',
            year=self.year,
            season=self.season,
        )

        # update county total hectares
        county_record.total_hectares = subcounty_records.aggregate(
            total=Sum('total_hectares')
        )['total'] or 0
        county_record.save()

        # recalculate each class total from subcounties
        class_totals = LandUseClass.objects.filter(
            record__in=subcounty_records
        ).values('name').annotate(
            total_hectares=Sum('hectares'),
            total_percentage=Sum('percentage')  # or recalculate from hectares
        )

        for ct in class_totals:
            LandUseClass.objects.update_or_create(
                record=county_record,
                name=ct['name'],
                defaults={
                    'hectares': ct['total_hectares'],
                    'percentage': round(
                        (ct['total_hectares'] / county_record.total_hectares) * 100, 2
                    ) if county_record.total_hectares else 0
                }
            )


class LandUseClass(models.Model):
    CLASS_CHOICES = [
        ('Crop', 'Crop'),
        ('Trees', 'Trees'),
        ('Building', 'Building'),
        ('Road', 'Road'),
        ('Shrub & Scrub', 'Shrub & Scrub'),
        ('Grass', 'Grass'),
        ('Water', 'Water'),
        ('Bare Ground', 'Bare Ground'),
    ]

    COLOR_MAP = {
        'Crop': '#ffff99',
        'Trees': '#00b050',
        'Road': '#d79e9e',
        'Building': '#ff0000',
        'Shrub & Scrub': '#ebf0d2',
        'Grass': '#a7d282',
        'Water': '#305496',
        'Bare Ground': '#b39e93',
    }

    record = models.ForeignKey(LandUseRecord, on_delete=models.CASCADE, related_name='classes')
    name = models.CharField(max_length=50, choices=CLASS_CHOICES)
    hectares = models.FloatField()
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.record} - {self.name}: {self.hectares}ha"

    @property
    def color(self):
        return self.COLOR_MAP.get(self.name, '#ffffff')  # no need to store in db, derived from name
    
    
class CropType(models.Model):
    CROPTYPE_COLORS = {
        'Coffee': '#7B3F00',
        'Maize': '#FFD700',
        'Beans': '#8B4513',
        'Tea': '#228B22',
        'Potato': '#DEB887',
        'Vegetables': '#90EE90',
        'Banana': '#FFE135',
        'Fruits': '#FF6347',
        'Cereals': '#F4A460',
        'Legumes': '#9ACD32',
    }

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    @property
    def color(self):
        return self.CROPTYPE_COLORS.get(self.name, '#ffffff')


class CropTypeRecord(models.Model):
    SEASON_CHOICES = [
        ('long_rains', 'Long Rains'),
        ('short_rains', 'Short Rains'),
    ]

    LEVEL_CHOICES = [
        ('county', 'County'),
        ('subcounty', 'Sub-County'),
    ]

    county = models.ForeignKey('Counties', on_delete=models.CASCADE, related_name='croptype_records', null=True, blank=True)
    subcounty = models.ForeignKey('Subcounties', on_delete=models.CASCADE, related_name='croptype_records', null=True, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='subcounty')
    year = models.IntegerField()
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, null=True, blank=True)
    total_hectares = models.FloatField()
    geoserver_wms_layername = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('county', 'subcounty', 'year', 'season')

    def __str__(self):
        area = self.subcounty or self.county
        return f"{area} - {self.year} ({self.get_season_display()})"

    def sync_county_totals(self):
        from django.db.models import Sum

        if self.level != 'subcounty' or not self.subcounty:
            return

        parent_county = Counties.objects.get(adm1_name=self.subcounty.adm1_name)

        county_record, _ = CropTypeRecord.objects.get_or_create(
            county=parent_county,
            subcounty=None,
            level='county',
            year=self.year,
            season=self.season,
            defaults={'total_hectares': 0, 'geoserver_wms_layername': self.geoserver_wms_layername}  # fixed
        )

        subcounty_records = CropTypeRecord.objects.filter(
            county=parent_county,
            level='subcounty',
            year=self.year,
            season=self.season,
        )

        county_record.total_hectares = subcounty_records.aggregate(
            total=Sum('total_hectares')
        )['total'] or 0
        county_record.save()

        class_totals = CropTypeClass.objects.filter(
            record__in=subcounty_records
        ).values('crop_type__name', 'crop_type').annotate(
            total_hectares=Sum('hectares'),
        )

        for ct in class_totals:
            CropTypeClass.objects.update_or_create(
                record=county_record,
                crop_type_id=ct['crop_type'],
                defaults={
                    'hectares': ct['total_hectares'],
                    'percentage': round(
                        (ct['total_hectares'] / county_record.total_hectares) * 100, 2
                    ) if county_record.total_hectares else 0
                }
            )


class CropTypeClass(models.Model):
    record = models.ForeignKey(CropTypeRecord, on_delete=models.CASCADE, related_name='classes')
    crop_type = models.ForeignKey(CropType, on_delete=models.PROTECT)  # PROTECT prevents deleting a crop that has data
    hectares = models.FloatField()
    percentage = models.FloatField()

    class Meta:
        unique_together = ('record', 'crop_type')

    def __str__(self):
        return f"{self.record} - {self.crop_type.name}: {self.hectares}ha"

    @property
    def color(self):
        return self.crop_type.color


    