from django import forms 
from models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
<<<<<<< HEAD
        
    
=======
        fields="__all__"
>>>>>>> master
