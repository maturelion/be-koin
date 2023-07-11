from rest_framework import serializers
from .models import Wallet, Currency, CurrencyBalance


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name", "icon", "symbol"]
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
    currency_set = CurrencySerializer(read_only=True, source="currency")

    class Meta:
        model = CurrencyBalance
        fields = [
            "id",
            "wallet",
            "currency",
            "currency_set",
            "balance",
            "show_pending"
        ]
        extra_kwargs = {
            "url":
                {
                    "view_name": "curency-balance-detail",
                    "lookup_field": "id"
                }
        }
