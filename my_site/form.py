from django import forms

from bootstrap_modal_forms.forms import BSModalForm

from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['fist_name', 'last_name', 'phone_number', 'email', 'comment']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'special'})
            self.fields['comment'].widget.attrs.update(size='40')



