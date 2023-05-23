from rest_framework import viewsets
from .models import Wallet, Currency, CurrencyBalance
from .serializers import WalletSerializer, CurrencySerializer, CurrencyBalanceSerializer
from rest_framework.permissions import BasePermission

class IsOwnerOrAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object or admin to view/edit it,
    but deny non-admin users from seeing the list of objects.
    """

    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    lookup_field = "id"
    http_method_names = ["get"]

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    lookup_field = "user"
    filterset_fields = ('user',)
    http_method_names = ["get"]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(user=self.request.user)
        return obj

class CurrencyBalanceViewSet(viewsets.ModelViewSet):
    queryset = CurrencyBalance.objects.all()
    serializer_class = CurrencyBalanceSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    lookup_field = "id"
    filterset_fields = ('wallet',)
    http_method_names = ["get"]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(user=self.request.user)
        return obj