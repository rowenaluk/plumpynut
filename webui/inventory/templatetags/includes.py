#!/usr/bin/env python
# vim: noet

from inventory.models import *
from django import template
register = template.Library()

@register.inclusion_tag("grid.html")
def incl_grid():
	return {"entries": Entry.objects.all()}

@register.inclusion_tag("messages.html")
def incl_messages(type):
	
	if type == "in":
		capt = "Incomming"
		og = False
		
	elif type == "out":
		capt = "Outgoing"
		og = True
	
	return {
		"caption": "Recent %s Messages" % (capt),
		"messages": Message.objects.filter(is_outgoing=og).order_by("-time")[:10]
	}
