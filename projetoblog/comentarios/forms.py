from pyexpat import model
from urllib import request
from django.forms import ModelForm
from .models import Comentario
import requests



class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        print(raw_data)
        recaptcha_response = raw_data.get('g-recaptcha-response')
        
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LeCfbUeAAAAAMW_wHDBnf1NLxvAoWLkkU0reUEx',
                'response':recaptcha_response
            }
        )
        recaptcha_resoult = recaptcha_request.json()
        if not recaptcha_resoult.get('success'):
            self.add_error('comentario', 'Desculpe Mr. Robot, ocorreu um erro.')
        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')
        
        if len(nome) <5:
            self.add_error('nome_comentario', 'O nome é muito curto')
            
    
    class Meta:
        model = Comentario
        fields = ('nome_comentario','email_comentario','comentario',)
    