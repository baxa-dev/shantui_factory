from django.contrib import admin
from .models import SpecialTechniqueCategory, SpecialTechnique, SpecialTechniqueApplication, Factory, \
    FactoryApplication, ServiceCenterRequest, Contact

@admin.register(SpecialTechniqueCategory)
class STCAdmin(admin.ModelAdmin):
	list_display = ("name", "top")


@admin.register(SpecialTechnique)
class STAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    filter_fields = ("category")
    list_display = ("name", "category")

admin.site.register(Factory)
admin.site.register(SpecialTechniqueApplication)
admin.site.register(FactoryApplication)
admin.site.register(ServiceCenterRequest)
admin.site.register(Contact)
