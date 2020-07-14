from django.db import models

class dado(models.Model):
    nome_fantasia = models.CharField(max_length=300)
    logomarca = models.ImageField(upload_to='logomarca', null=True, blank=True)
    endereço = models.CharField(max_length=300)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=11)
    horario_de_atendimento = models.CharField(max_length=20)
    nome_do_proprietário = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone_fixo = models.CharField(max_length=11)
    celular_whatsapp = models.CharField(max_length=11)
    breve_descrição_da_empresa = models.TextField()

    def __str__(self):
        return self.nome_fantasia


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
    Informações_sobre_o_serviço = models.TextField(max_length=50)
    preço = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nome_do_serviço