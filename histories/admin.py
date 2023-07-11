from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import History


class HistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "user",
        "currency",
        "amount",
        "tx_type",
        "created_at"
    ]


admin.site.register(History, HistoryAdmin)
