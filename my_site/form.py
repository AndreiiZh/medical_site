from django import forms

from bootstrap_modal_forms.forms import BSModalForm

from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['fist_name', 'last_name', 'email', 'phone_number', 'comment']






