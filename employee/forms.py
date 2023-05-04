from django import forms
from django.core.exceptions import ValidationError
from .models import Car, CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'registration_number', 'year', 'doors', 'seats', 'ac', 'gearbox',
            'fuel', 'picture', 'car_model'
        ]
        widgets = {
            'car_model': forms.Select(attrs={'class': 'form-select'}),
            'gearbox': forms.RadioSelect(attrs={'class': 'form-check-inline'}),
            'fuel': forms.RadioSelect(attrs={'class': 'form-check-inline'}),
        }

    def clean_registration_number(self):
        registration_number = self.cleaned_data['registration_number']
        if not registration_number.isalnum():
            raise ValidationError('Registration number must contain only letters and numbers.')
        return registration_number


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car_brand'].widget.attrs['class'] = 'form-select'
