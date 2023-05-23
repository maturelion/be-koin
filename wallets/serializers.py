from rest_framework import serializers
from .models import Wallet, Currency, CurrencyBalance


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name", "symbol"]
        extra_kwargs = {
            "url": {"view_name": "currency-detail", "lookup_field": "id"}
        }

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "user", "currencies"]
        extra_kwargs = {
            "url": {"view_name": "wallet-detail", "lookup_field": "user"}
        }

class CurrencyBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyBalance
        fields = ["id", "wallet", "currency", "balance"]
        extra_kwargs = {
            "url": {"view_name": "curency-balance-detail", "lookup_field": "id"}
        }