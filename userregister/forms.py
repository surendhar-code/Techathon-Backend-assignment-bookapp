from django import forms 
from .models import book


class BookForm(forms.ModelForm):

    class Meta:
        model=book
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(BookForm,self).__init__(*args,**kwargs)
        self.fields['genre'].empty_label= "Select"