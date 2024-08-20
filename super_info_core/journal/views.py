from django.core.paginator import Paginator
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView
from journal.models import Publication, PublicationComment, AboutMe
# from django.shortcuts import render, redirect
# from journal.telegram import bot


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publications = Publication.objects.all()
        paginator = Paginator(publications, 1)


        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context

class HomeSearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        search_word = self.request.GET['search']
        context = {
            'publication_list': Publication.objects.filter(is_active=True).filter(
                Q(title__icontains=search_word) | Q(description__icontains=search_word)
            )
        }
        return context


class PublicationView(TemplateView):
    template_name = 'publication-detail.html'


class AboutView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = {
            'about_me': AboutMe.objects.first()
        }
        return context

    def post(request, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)
        commant_text = request.POST['comment_text']
        PublicationComment.objects.create(publication=publication, text=commant_text)
        bot.send_message(chat_id=1723863989, text='Для вашей публикации написали комментрий. Не забудь проверить!')
        return request('publication-detail.html', publication_pk),

class CreatePublicationCommentView(View):
    pass
