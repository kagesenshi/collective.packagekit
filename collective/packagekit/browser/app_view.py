from five import grok
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior

grok.templatedir('templates')

class AppView(grok.View):
    grok.name('index')
    grok.context(IPackageKitApplicationBehavior)
    grok.template('app_view')

