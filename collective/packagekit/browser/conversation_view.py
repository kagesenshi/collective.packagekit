from five import grok
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior

class ConversationView(grok.View):
    grok.name('conversation_view')
    grok.context(IPackageKitApplicationBehavior)

    def enabled(self):
        return True

    def render(self):
        return str(self)
