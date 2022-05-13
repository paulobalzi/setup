from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
