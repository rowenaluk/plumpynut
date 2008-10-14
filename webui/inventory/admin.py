#!/usr/bin/env python
# vim: noet

from django.contrib import admin
from models import *
from forms import *


class MonitorAdmin(admin.ModelAdmin):
	form = MonitorForm
	list_display = ('full_name', 'alias', 'phone', 'email')

class EntryInline(admin.TabularInline):
	model = Entry

class EntryAdmin(admin.ModelAdmin):
	list_display = ('supply_location', 'time', 'monitor')
	list_filter = ['time']
	date_hierarchy = 'time'
	ordering = ['time']	

class LocationInline(admin.TabularInline):
	form = LocationForm
	model = Location

class AreaInline(admin.TabularInline):
	model = Area

class AreaAdmin(admin.ModelAdmin):
	list_display = ('name', 'number_of_locations')
	inlines = [LocationInline,]

class LocationAdmin(admin.ModelAdmin):
	form = LocationForm
	list_display = ('name', 'code', 'area')

class ZoneAdmin(admin.ModelAdmin):
	inlines = [AreaInline, ]

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
	list_display = ('supply', 'begin_date', 'end_date', 'number_of_entries', 'latest_entry')
	list_filter = ['begin_date']
	radio_fields = {'supply' : admin.HORIZONTAL}

class SupplyAdmin(admin.ModelAdmin):
	form = SupplyForm
	list_display = ('name', 'code', 'number_of_reports')
	inlines = [ReportInline,]

class SupplyLocationAdmin(admin.ModelAdmin):
	list_display = ('location', 'supply', 'quantity', 'area')
	radio_fields = {'supply' : admin.HORIZONTAL}
	inlines = [EntryInline,]


# add our models to the django admin
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Zone, ZoneAdmin)
#admin.site.register(Location, LocationAdmin)
admin.site.register(SupplyLocation, SupplyLocationAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Entry, EntryAdmin)
