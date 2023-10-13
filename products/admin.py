from django.contrib import admin
from products.models import products
from django.utils.html import format_html
from django.contrib.auth.models import User

class customAdmin(admin.ModelAdmin):
    list_display = ['product_name','image_tag','product_company_name']

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:100px; height:100px; border-radius:10%; object-fit:cover"/>',obj.product_image.url)


# Register your models here.
admin.site.register(products,customAdmin)
admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Admin'
admin.site.index_title = 'medical app Administrator'