from django import forms

class UploadFileForm(forms.Form):
    """
    Simplest of forms to provide file upload
    """
    title = forms.CharField(max_length=50)
    file = forms.FileField()