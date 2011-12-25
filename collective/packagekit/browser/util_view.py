from five import grok
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior
from zope.interface import Interface
from itertools import izip

grok.templatedir('templates')

from zope.security import checkPermission

class PKAppUtilView(grok.View):
    grok.name('pkapp_util')
    grok.context(IPackageKitApplicationBehavior)

    def render(self):
        return str(self)

    def gridslice(self, items, size=5):
        l = items
        n = size
#       http://taylanpince.com/blog/posts/slicing-a-list-into-equal-groups-in-python/
        return [s for s in izip(*[iter(l)] * n)] + [l[len(l) - (len(l) % n):]]

    def fedora_packages(self):
        pkgs = [i['identifier'] for i in self.context.pk_packages if (
                i['distribution'] == 'fedora')]
        return set(pkgs)


    def images(self):
        return self.context.portal_catalog(
            path={
                'query': '/'.join(self.context.getPhysicalPath()),
                'depth': 1
            },
            portal_type='Image'
        )

    def can_add(self):
        return checkPermission('cmf.AddPortalContent', self.context)

