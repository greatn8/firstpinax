from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from newsite import views
from .views import ChartData


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^index/", views.index, name='index'),
    url(r"^api/chart/data/", ChartData.as_view(), name='api-data'),
    url(r"^chart/", views.ChartView, name='ChartView')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
