from five import grok
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior

grok.templatedir('templates')

class AppView(grok.View):
    grok.name('view')
    grok.context(IPackageKitApplicationBehavior)
    grok.template('app_view')

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
