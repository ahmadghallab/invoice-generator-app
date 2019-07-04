from django import forms
from . import models

# Stock
class StockForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['name','code','price']
        widgets = {
            'name': forms.TextInput(attrs={
               'autocomplete': 'off',
               'placeholder': 'Item name', 
            }),
            'code': forms.TextInput(attrs={
               'autocomplete': 'off',
               'placeholder': 'Material Number', 
            }),
            'price': forms.NumberInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Item Price'
            })
        }

# Service categories
class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ServiceCategory
        fields = ['ar_name']
        widgets = {
            'ar_name': forms.TextInput(attrs={
                'autocomplete': 'off'
            })
        }
    def __init__(self, *args, **kwargs):
        super(ServiceCategoryForm, self).__init__(*args, **kwargs)
        self.fields['ar_name'].label = "Name"

# Vehilces
class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = ['ar_name']
        widgets = {
            'ar_name': forms.TextInput(attrs={
                'autocomplete': 'off'
            })
        }
    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['ar_name'].label = "Name"

# Customers
class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['ar_name','address','telephone','vehicle','vin','engine','license_plate']
        widgets = {
            'ar_name': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Customer Arabic Name'
            }),
            'address': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Customer Address'
            }),
            'telephone': forms.NumberInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Customer Telephone'
            }),
            'vin': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Vehicle Vin Number'
            }),
            'engine': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Vehicle Engine Number'
            }),
            'license_plate': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Vehicle License Plate Number'
            })
        }
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['ar_name'].label = "Name"

# Order
class OrderForm(forms.ModelForm):
    customer_call = forms.BooleanField()
    class Meta:
        model = models.Order
        fields = ['enter_date','exit_date','enter_time','exit_time','customer_call','type','vehicle_counter','complaint','notes']

# Bill
class BillForm(forms.ModelForm):
    tax = forms.BooleanField()
    class Meta:
        model = models.Bill
        fields = ['date','type','item_code','description','price','qty','discount','tax']
