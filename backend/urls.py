from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from histories.views import HistoryViewSet
from users.views import UserViewSet
from wallets.views import (
    WalletViewSet,
    CurrencyViewSet,
    CurrencyBalanceViewSet
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"wallets", WalletViewSet, basename="wallet")
router.register(r"histories", HistoryViewSet, basename="history")
router.register(r"currencies", CurrencyViewSet, basename="currency")
router.register(
    r"currency-balances",
    CurrencyBalanceViewSet,
    basename="currency-balance"
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("rest-auth/", include("dj_rest_auth.urls")),
    path("rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("accounts/", include("allauth.urls")),
    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT}
    ),
    re_path(
        r'^static/(?P<path>.*)$',
        serve,
        {'document_root': settings.STATIC_ROOT}
        ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
