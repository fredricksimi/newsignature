from django import forms
from .models import SignatureTool

class UserDetailsForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Names"}))
    company = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Company"}))
    designation = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Designation"}))
    department = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Department"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"Phone":"Phone"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
    website = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Website"}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Facebook"}), required=False)
    linkedin = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"LinkedIn"}), required=False)
    twitter = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Twitter"}), required=False)
    github = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"GitHub"}), required=False)
    instagram = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Instagram"}), required=False)
    whatsapp = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"WhatsApp"}), required=False)
    youtube = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"YouTube"}), required=False)
    
    class Meta:
        model = SignatureTool
        fields = '__all__'
