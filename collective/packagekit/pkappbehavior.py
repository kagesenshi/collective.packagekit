from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective.packagekit import MessageFactory as _


class IPackageKitApplicationBehavior(form.Schema):
    """
       Marker/Form interface for PackageKit Application Behavior
    """
   
    # -*- Your Zope schema definitions here ... -*-

    pk_packages = schema.List(
        title=u'Packages',
        description=(u'List of packages related for this application, separate'
                     u' using newline'),
        value_type=schema.TextLine(title=u'Package')
    )


alsoProvides(IPackageKitApplicationBehavior,IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)

class PackageKitApplicationBehavior(object):
    """
       Adapter for PackageKit Application Behavior
    """
    implements(IPackageKitApplicationBehavior)
    adapts(IDexterityContent)

    pk_packages = context_property('pk_packages')

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
