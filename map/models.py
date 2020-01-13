import re
from django.db import models
from django import forms
# from geoposition.fields import GeopositionField


# class Zone(models.Model):
# name = models.CharField(max_length=50)
# An Apostrophe that use for blank data between
# latitude and longitude.
# an_apostrophe = models.CharField(max_length=3)
# Knot Number (by Kilometer)
# Knot_Number = models.CharField(max_length=5)
# Explain about some places you pined
# description = models.CharField(max_length=300)
# address = models.CharField(max_length=100)
# position = GeopositionField()


# class Show_Location(models.Model):
#     # location_title = models.CharField(max_length=100)
#     lnglat = models.CharField(max_length=40, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     # def __str__(self):
#     #     return self.location_title
def lnglat_validator(value):
    if not re.match(r'^[+-]?\d+\.?\d*,[+-]?\d+\.?\d*$', value):
        raise forms.ValidationError('경도와 위도를 입력해주세요')


class Post(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    lnglat = models.CharField(max_length=40, blank=True, validators=[lnglat_validator])
    # is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]
        return None

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]
        return None
