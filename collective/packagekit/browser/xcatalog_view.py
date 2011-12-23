from five import grok
from collective.packagekit.pkappbehavior import IPackageKitApplicationBehavior

class XCatalogView(grok.View):
    grok.context(IPackageKitApplicationBehavior)
    grok.name('download_catalog')

    def render(self):
        self.request.response.setHeader('Content-type', 'application/x-catalog')

        items = {}
        for pkg in self.context.pk_packages:
            distid = pkg['distribution']
            if pkg['release']:
                distid = '%s;%s' % (distid, pkg['release'])
            items.setdefault(distid, [])
            items[distid].append(pkg['identifier'])

        result =  '[PackageKit Catalog]\n'

        for key, value in items.items():
            result += '\nInstallPackages(%s)=%s\n' % (key, ';'.join(value))

        self.request.response.setHeader('Content-Length',len(result))
        self.request.response.setHeader('Content-disposition', 
                                    'inline;filename=%s.catalog' %
                                    self.context.id)
        return result
