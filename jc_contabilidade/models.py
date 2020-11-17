from django.db import models
from django import forms


class dado(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    atuação = (
        ('Academia', 'Academia'), ('Açougue', 'Açougue'), ('Armarinhos', 'Armarinhos'), ('Auto peças', 'Auto peças'),
        ('Barbearia', 'Barbearia'), ('Distribuidora de bebidas', 'Distribuidora de bebidas'),
        ('Farmácia', 'Farmácia'), ('Ferragista', 'Ferragista'), ('Lanchonete', 'Lanchonete'),
        ('Loja de artigos para celulares', 'Loja de artigos para celulares'), ('Loja de calçados', 'Loja de calçados'),
        ('Loja de roupas', 'Loja de roupas'),
        ('Mercearia', 'Mercearia'), ('Panificadora', 'Panificadora'),
        ('Papelaria', 'Papelaria'), ('Pet Shop', 'Pet Shop'), ('Prestação de serviços', 'Prestação de serviços'),
        ('Restaurante', 'Restaurante'), ('Salão de beleza', 'Salão de beleza'), ('Supermercado', 'Supermercado'),
        ('Serviços de Advocacia', 'Serviços de Advocacia'), ('Serviços Contábeis', 'Serviços Contábeis'),
        ('Serviços Gerais', 'Serviços Gerais'), ('Serviços de Informática', 'Serviços de Informática'),
        ('Oficina de automóveis', 'Oficina de automóveis'), ('Outros', 'Outros'),)
    atividade = models.CharField(max_length=100, choices=atuação)
    logomarca = models.ImageField(upload_to='logomarca', null=True, blank=True)
    endereço = models.CharField(max_length=300)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    federações = (
        ('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'),
        ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'),
        ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'),
        ('PI', 'PI'), ('SE', 'SE'), ('TO', 'TO'))
    estado = models.CharField(max_length=50, null=True, blank=True, choices=federações)
    cnpj = models.CharField(max_length=11)
    horario_de_atendimento = models.CharField(max_length=20)
    nome_do_proprietário = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone_fixo = models.CharField(max_length=11, null=True, blank=True)
    celular_whatsapp = models.CharField(max_length=11)
    anunciar = (
        ('Produtos', 'Produtos'),
        ('Serviços', 'Serviços'),
        ('Produtos e serviços', 'Produtos e serviços'),
    )
    tenho_interesse_em_anunciar = models.CharField(max_length=50, null=True, blank=True, choices=anunciar)
    breve_descrição_da_empresa = models.TextField()
    palavras_chave = models.CharField(max_length=100, null=True, blank=True)
    observações = models.CharField(max_length=100, null=True, blank=True)


def __str__(self):
    return str(self.nome_fantasia)


class produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome_do_produto = models.CharField(max_length=30)
    imagem_do_produto = models.ImageField(upload_to='produtos', null=True, blank=True)
    Informações_sobre_o_produto = models.TextField(max_length=50)
    preço = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome_do_produto


class serviço(models.Model):
    nome_do_serviço = models.CharField(max_length=30)
    imagem_do_serviço = models.ImageField(upload_to='serviços', null=True, blank=True)
    Informações_sobre_o_serviço = models.TextField(max_length=200)
    preço = models.FloatField( null=True, blank=True)

    def __str__(self):
        return self.nome_do_serviço