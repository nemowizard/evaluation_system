from django.contrib import admin
from .models import QualEval

class QualEvalAdmin(admin.ModelAdmin):
    search_fields = ['ID_num']

admin.site.register(QualEval, QualEvalAdmin)
