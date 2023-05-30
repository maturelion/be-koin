from django.contrib import admin
from .models import Wallet, Currency, CurrencyBalance
from import_export.admin import ImportExportModelAdmin


class CurrencyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "symbol"]



class WalletAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["user__username"]
    list_display = ["user"]

class CurrencyBalanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # search_fields = ["user__username"]
    list_display = [
        "wallet",
        "currency",
        "balance",
        "show_pending",
    ]


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyBalance, CurrencyBalanceAdmin)
admin.site.register(Wallet, WalletAdmin)