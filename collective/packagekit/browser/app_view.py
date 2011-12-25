from five import grok
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior
from zope.security import checkPermission

grok.templatedir('templates')

class AppView(grok.View):
    grok.name('view')
    grok.context(IPackageKitApplicationBehavior)
    grok.template('app_view')
