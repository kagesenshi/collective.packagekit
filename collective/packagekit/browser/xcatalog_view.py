from five import grok
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior

class XCatalogView(grok.View):
    grok.context(IPackageKitApplicationBehavior)
    grok.name('download_catalog')

    def render(self):
        self.request.response.setHeader('Content-type', 'application/x-catalog')
        result =  '''
        [PackageKit Catalog]

        InstallPackages(fedora)=%s
        ''' % ';'.join(self.context.pk_packages)

        self.request.response.setHeader('Content-Length',len(result))
        self.request.response.setHeader('Content-disposition', 
                                    'inline;filename=%s.catalog' %
                                    self.context.id)
        return result
