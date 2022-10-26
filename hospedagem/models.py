from django.db import models

# Create your models here.
class Tipo_Quarto(models.Model):
    descricao = models.TextField("Descrição");
    valor_diaria = models.DecimalField('Valor da diária', max_digits=8, decimal_places=2)
    imagem_quarto = models.ImageField("Imagem", upload_to='quarto/');

    class Meta:
        verbose_name_plural = "Tipo do quarto";

class Estadia(models.Model):
    nome_cliente = models.CharField("Nome", max_length=100);
    data_entrada = models.DateField("Data de entrada");
    data_saida = models.DateField("Data de saída");
    valor_total = models.DecimalField('Valor total', max_digits=8, decimal_places=2)
    tipo_quarto = models.ForeignKey(Tipo_Quarto, on_delete=models.CASCADE);

    class Meta:
        verbose_name_plural = "Estadia";

