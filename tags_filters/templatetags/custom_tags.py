# -*- coding: utf-8 -*-
from django import template
from alkawsarsite import util

register = template.Library()

@register.filter
def bengalinumber(value):
    return util.convert_e2b(value)