from django import forms

class EditRecipeForm(forms.Form):
    addrecipe = forms.CharField(label='Add Recipe', max_length=100)