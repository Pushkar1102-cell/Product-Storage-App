from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'minlength': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Product Name must be at least 3 characters long.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if not description.strip():
            raise forms.ValidationError("Description cannot be empty.")
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price
