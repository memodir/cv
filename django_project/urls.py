from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.i18n import JavaScriptCatalog
from django.utils.translation import ugettext_lazy as _

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += ([
    url(r'^$', RedirectView.as_view(url='main/'), name='home'),
    url(r'^main/', include('resume.urls')),

])

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
