from django import forms



class QRCOdeForm(forms.Form):
    restaurant_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Restaurant name'
    })
    )
    url=forms.URLField(max_length=200,label='Menu URL',widget=forms.URLInput(attrs={
           'class ':'form-control',
           'placeholder': 'Enter th URl of your online menu'
    })
    )