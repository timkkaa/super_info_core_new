from modeltranslation.translator import register, TranslationOptions

from journal.models import Category, Publication

@register(Category)
class CatigoryTranslationpOtions(TranslationOptions):
    fieild = ('title',)

@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fieild = ('title', 'descripyion')

