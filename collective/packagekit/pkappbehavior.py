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
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow

from collective.packagekit.vocabulary import GROUPS_VOCABULARY

def checkImageSize(value):
    geometry = (value._height, value._width)

    if geometry not in [
            (96, 96),
            (128, 128), 
            (256,256)]:
        return False

    return True


class IPackageKitPackages(form.Schema):
    identifier = schema.TextLine(
        title=u'Package'
    )

    distribution = schema.Choice(
        title=u'Distribution',
        values=['fedora', 'ubuntu', 'debian'],
    )
    release = schema.TextLine(
        title=u'Distribution Release',
        required=False
    )

class IPackageKitApplicationBehavior(form.Schema):
    """
       Marker/Form interface for PackageKit Application Behavior
    """
   
    # -*- Your Zope schema definitions here ... -*-

    pk_icon = namedfile.NamedBlobImage(
        title=u'Icon',
        description=u'valid sizes are 96x96, 128x128, and 256x256',
        constraint=checkImageSize
    )

    form.widget(pk_packages=DataGridFieldFactory)
    pk_packages = schema.List(
        title=u'Packages',
        description=(u'List of packages related for this application. ' +
        'Distribution Release is optional'),
        value_type=DictRow(title=u'Package', schema=IPackageKitPackages)
    )

    pk_categories = schema.List(
        title=u'Categories',
        value_type=schema.Choice(
            title=u'Category',
            vocabulary=GROUPS_VOCABULARY
        )
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
    pk_icon = context_property('pk_icon')
    pk_categories = context_property('pk_categories')

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
