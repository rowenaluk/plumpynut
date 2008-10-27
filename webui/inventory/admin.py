#!/usr/bin/env python
# vim: noet

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from models import *
from forms import *


class MonitorAdmin(admin.ModelAdmin):
	form = MonitorForm
	list_display = ('__unicode__', 'alias', 'phone', 'email')
	search_fields = ('__unicode__', 'alias')


class EntryInline(admin.TabularInline):
	model = Entry


class EntryAdmin(admin.ModelAdmin):
	list_display = ('supply_place', 'time', 'monitor')
	list_filter = ['time']
	date_hierarchy = 'time'
	ordering = ['time']	
	search_fields = ('supply_place', 'monitor')


class LocationInline(admin.TabularInline):
	model = Location


class AreaInline(admin.TabularInline):
	model = Area

class AreaAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'zone', 'number_of_OTPs')
	search_fields = ('name', 'code', 'zone')
	inlines = [LocationInline,]

class LocationAdmin(admin.ModelAdmin):
	verbose_name = "OTP"
	list_display = ('name', 'code', 'woreda')
	search_fields = ('name', 'code', 'woreda')

class ZoneAdmin(admin.ModelAdmin):
	list_display = ('name', 'region', 'number_of_woredas')
	radio_fields = {'region' : admin.HORIZONTAL}
	search_fields = ('name', 'region')
	inlines = [AreaInline, ]

class RegionAdmin(admin.ModelAdmin):
	list_display = ('name', 'number_of_zones')

class NotificationAdmin(admin.ModelAdmin):
	list_display = ('monitor', 'time', 'resolved', 'notice')
	list_filter = ['resolved', 'time']
	date_hierarchy = 'time'
	ordering = ['resolved']

class ReportInline(admin.TabularInline):
	list_display = ('supply', 'begin_date', 'end_date', 'number_of_entries', 'latest_entry')
	list_filter = ['begin_date']
	model = Report

class ReportAdmin(admin.ModelAdmin):
	list_display = ('supply', 'begin_date', 'end_date', 'number_of_entries', 'latest_entry', 'export_link')
	list_filter = ['begin_date']
	radio_fields = {'supply' : admin.HORIZONTAL}

	def export_link(self, instance):
		return "/export/%d/"

class SupplyAdmin(admin.ModelAdmin):
	form = SupplyForm
	list_display = ('name', 'code', 'number_of_reports')
	#inlines = [ReportInline,]

class SupplyPlaceAdmin(admin.ModelAdmin):
	list_display = ('location', 'supply', 'quantity', 'woreda')
	radio_fields = {'supply' : admin.HORIZONTAL}
	#inlines = [EntryInline,]


# add our models to the django admin
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SupplyPlace, SupplyPlaceAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Entry, EntryAdmin)

