from django.contrib import admin
from .models import dado, produto, serviço


class dadoAdmin(admin.ModelAdmin):
    list_display = ['nome_fantasia', 'endereço', 'telefone_fixo', 'celular_whatsapp']

class produtoAdmin(admin.ModelAdmin):
    list_display = ['nome_do_produto', 'preço']
    search_fields = ['nome_do_produto', 'preço']

class serviçoAdmin(admin.ModelAdmin):
    list_display = ['nome_do_serviço', 'preço']
    search_fields = ['nome_do_serviço', 'preço']

'''
admin.site.register(dado, dadoAdmin)
admin.site.register(produto, produtoAdmin)
admin.site.register(serviço, serviçoAdmin)
'''