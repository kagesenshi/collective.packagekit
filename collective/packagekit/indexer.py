
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior
from plone.indexer import indexer

@indexer(IPackageKitApplicationBehavior)
def categories(obj):
    return getattr(obj, 'pk_categories', [])
