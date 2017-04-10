#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint
from django import template

register = template.Library()

@register.simple_tag
def random(begin, end):
    try:
      return randint(int(begin), int(end))
    except Exception as e:
      raise e + "Deux arguments int sont nécessaire"
