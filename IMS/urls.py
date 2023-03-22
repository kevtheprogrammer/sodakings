from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from product.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(IndexView.as_view()),name='index'),
    path("admin/", admin.site.urls),
    path("products/", include('product.urls')),
    path("auth/", include('acc.urls')),
    path("transactions/", include('transactions.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
