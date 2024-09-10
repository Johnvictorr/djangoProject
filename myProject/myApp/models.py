from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    nascimento = models.DateField(null=True)
    email = models.EmailField(null=True, max_length=254)
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True)
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome