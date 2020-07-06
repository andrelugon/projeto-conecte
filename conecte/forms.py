from django.forms import ModelForm
from .models import cliente

class clienteForm(ModelForm):
    class Meta:
        model = cliente
        fields = ['nome_fantasia',
                  'atividade',
                  'endereço',
                  'bairro',
                  'cidade',
                  'estado',
                  'cnpj',
                  'horario_de_atendimento',
                  'nome_do_proprietário',
                  'sobrenome',
                  'email',
                  'telefone_fixo',
                  'celular_whatsapp',
                  'breve_descrição_da_empresa',
                  'tenho_interesse_em_anunciar',
                  'observações',
                  'logomarca',

                  ]

