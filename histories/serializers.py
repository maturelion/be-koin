from rest_framework.serializers import ModelSerializer

from wallets.serializers import CurrencySerializer
from .models import History


class HistorySerializer(ModelSerializer):
    currency_set = CurrencySerializer(read_only=True, source="currency")

    class Meta:
        model = History
        fields = [
            "id",
            "user",
            "currency",
            "currency_set",
            "amount",
            "tx_type",
            "created_at"
        ]
        extra_kwargs = {
            "url": {
                "view_name": "history-detail",
                "lookup_field": "id"
            }
        }
