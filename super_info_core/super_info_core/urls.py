from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from journal.views import AboutView, HomeView, PublicationView, CreatePublicationCommentView, HomeSearchView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('home/', HomeView.as_view(), name='home-url'),
    path('home/search/',HomeSearchView.as_view(), name='home-search-url'),
    path('publication/<int:pk>/', PublicationView.as_view(), name='publication-detail-url'),
    path('about/', AboutView.as_view(), name='about-url'),
    path('publication-detail/<int:pk>/create-commant/', CreatePublicationCommentView.as_view()),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)