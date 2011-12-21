from five import grok
from Products.ATContentTypes.interfaces.topic import IATTopic
from zope.interface import Interface
from itertools import izip

grok.templatedir('templates')

class PKAppUtilView(grok.View):
    grok.name('pkapp_util')
    grok.context(Interface)

    def render(self):
        return str(self)

    def gridslice(self, items, size=5):
        l = items
        n = size
#       http://taylanpince.com/blog/posts/slicing-a-list-into-equal-groups-in-python/
        return [s for s in izip(*[iter(l)] * n)] + [l[len(l) - (len(l) % n):]]
