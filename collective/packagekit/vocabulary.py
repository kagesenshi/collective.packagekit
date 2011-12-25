from zope.schema.vocabulary import SimpleVocabulary
from collective.packagekit import MessageFactory as _

GROUPS=[
    ('admin-tools',_('Admin tools')),
    ('desktop-gnome',_('GNOME desktop')),
    ('desktop-kde',_('KDE desktop')),
    ('desktop-other',_('Other desktops')),
    ('desktop-xfce',_('XFCE desktop')),
    ('education',_('Education')),
    ('fonts',_('Fonts')),
    ('games',_('Games')),
    ('graphics',_('Graphics')),
    ('internet',_('Internet')),
    ('legacy',_('Legacy')),
    ('localization',_('Localization')),
    ('multimedia',_('Multimedia')),
    ('office',_('Office')),
    ('other',_('Other')),
    ('programming',_('Programming')),
    ('publishing',_('Publishing')),
    ('servers',_('Servers')),
    ('system',_('System')),
    ('virtualization',_('Virtualization')),
    ('collections',_('Collections')),
]

GROUPS_VOCABULARY=SimpleVocabulary.fromItems(GROUPS)
