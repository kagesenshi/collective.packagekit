from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior


class IPackageKitWebPortlet(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    """Portlet assignment."""

    implements(IPackageKitWebPortlet)

    @property
    def title(self):
        return u"PackageKit Portlet"

class Renderer(base.Renderer):
    """ Portlet renderer. """

    render = ViewPageTemplateFile("pkwebportlet.pt")

    @property
    def available(self):
        if not IPackageKitApplicationBehavior.providedBy(self.context):
            return False
        if getattr(self.context, 'pk_packages', []):
            return True
        return False

class AddForm(base.NullAddForm):
    """ Portlet add form. """

    def create(self):
        return Assignment()
