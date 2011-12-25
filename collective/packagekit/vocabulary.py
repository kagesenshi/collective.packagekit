from zope.schema.vocabulary import SimpleVocabulary
from collective.packagekit import MessageFactory as _
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory

GROUPS=[
   (_('Admin tools'), 'admin-tools'),
   (_('GNOME desktop'), 'desktop-gnome'),
   (_('KDE desktop'), 'desktop-kde'),
   (_('Other desktops'), 'desktop-other'),
   (_('XFCE desktop'), 'desktop-xfce'),
   (_('Education'), 'education'),
   (_('Fonts'), 'fonts'),
   (_('Games'), 'games'),
   (_('Graphics'), 'graphics'),
   (_('Internet'), 'internet'),
   (_('Legacy'), 'legacy'),
   (_('Localization'), 'localization'),
   (_('Multimedia'), 'multimedia'),
   (_('Office'), 'office'),
   (_('Other'), 'other'),
   (_('Programming'), 'programming'),
   (_('Publishing'), 'publishing'),
   (_('Servers'), 'servers'),
   (_('System'), 'system'),
   (_('Virtualization'), 'virtualization'),
   (_('Collections'), 'collections'),
]

GROUPS_VOCABULARY=SimpleVocabulary.fromItems(GROUPS)

def groups_vocabulary_factory(context):
    return GROUPS_VOCABULARY
