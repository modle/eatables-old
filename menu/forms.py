from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select file')

# class DocumentForm(forms.Form):
    # docfile = forms.FileField(widget=forms.FileField(attrs={'class' : 'fileUpload'}))
