from django.db import models


class Calculator(models.Model):
    age = models.IntegerField('age')
    monthly_income = models.IntegerField('ежемесячный доход')
    inflation = models.IntegerField('инфляция')
    monthly_cost = models.IntegerField('расходы')
    Airbag = models.IntegerField('подушка безопасности')
    amount_of_capital = models.IntegerField('текущий размер капитала')
