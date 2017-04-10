#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()

@register.tag
def fifo(parser, token):
    """Généère une liste de nombre dans un interval qui va permettre.
    token : contient plusieur sinformation dont les arguments ainsi que plusieurs méthode facilitant le traiement
    parser: élément qui va traiter notre tag lorsqu'il est capturé dans notre template.

    """

    try:
      tag_name, min, max = token.split_contents()
    except:
      msg = "Le tag %s doit prendre deux arguments" % token.split_contents()[0]
      raise template.TemplateSyntaxError(msg)

    return FifoNode(min, max)

class FifoNode(template.Node):

    def __init__(self, min, max):
      self.min = min
      self.max = max

    def generateListNumber(self):
      list = []

      for i in xrange(self.min,self.max):
        list.append(str(i))

      return list

    def render(self, context):
      """Rend le noeud, si tout est bon. Un check au départ permet gérer toutes les erreurs en one shot"""

      not_exist = False

      try:
        min = template.Variable(self.min).resolve(context) # Si la variable n'est pas trouvé on retient la constante...
        self.min = int(min) # ...que l'onconvertie en Int
      except (VariableNotExist, ValueError):
        not_exist = self.min

      try:
        max = template.Variable(self.max).resolve(context)
        self.max = int(max)
      except (VariableNotExist, ValueError):
        not_exist = self.max

      if not_exist:
        msg = "Le tag %s doit prendre deux arguments" % token.split_contents()[0]
        msg = msg + "L'argument %s n'est pas complet" % not_exist
        raise template.TemplateSyntaxError(msg)

      if self.min > self.max:
        msg = "self.min > self.max"
        raise template.TemplateSyntaxError(msg)

      return ' '.join(self.generateListNumber())
