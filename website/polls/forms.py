from django import forms
from polls import models
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput

# class ProductForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         """ Grants access to the request object so that only members of the current user
#         are given as options"""

#         self.user = kwargs.pop('username', None)
#         super(ProductForm, self).__init__(*args, **kwargs)
#         self.fields['user'].queryset = models.Users.objects.filter(
#             user=self.user)
#         return 

        
#     user = forms.ModelChoiceField(queryset=None, empty_label=None)
#     product = forms.CharField(max_length=200)
#     monthly = forms.IntegerField()
#     pub_date = forms.DateTimeField(
#         widget=DatePickerInput
#     )
#     class Meta:
#         model = models.ClientProductData
#         fields = [
#             'user', 'product', 'monthly', 'pub_date'
#         ]

class ProductDataForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.user = kwargs.pop('username', None)
        super(ProductDataForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = models.Users.objects.filter(
            user=self.user)
        return 
    
    choice = models.ProductData.objects.all()
    user = forms.ModelChoiceField(queryset=None, empty_label=None)
    productid = forms.CharField(max_length=200)
    product_name = forms.CharField(max_length=200)
    unit_price = forms.IntegerField()

    class Meta:
        model = models.ProductData
        fields = [
            'user','productid', 'product_name', 'unit_price'
        ]

class StoreDataForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.user = kwargs.pop('username', None)
        super(StoreDataForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = models.Users.objects.filter(
            user=self.user)
        return 

    user = forms.ModelChoiceField(queryset=None, empty_label=None)
    storeid = forms.CharField(max_length=200)
    store_name = forms.CharField(max_length=200)
    store_location = forms.CharField(max_length=200)

    class Meta:
        model = models.StoreData
        fields = [
            'user','storeid', 'store_name', 'store_location'
        ]

class SalesDataForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""
        self.user = kwargs.pop('username', None)
        self.user_id = models.Users.objects.get(user=self.user)
        super(SalesDataForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = models.Users.objects.filter(
            user=self.user)
        self.fields['prodid'].queryset = models.ProductData.objects.filter(
            user=self.user_id)
        self.fields['storeid'].queryset = models.StoreData.objects.filter(
            user=self.user_id)
        return 
 
    user = forms.ModelChoiceField(queryset=None, empty_label=None)
    prod_d = forms.ModelChoiceField(queryset=None)
    storeid = forms.ModelChoiceField(queryset=None)
    pub_date = forms.DateTimeField(
        widget=DatePickerInput
    )
    units_sold = forms.IntegerField()

    class Meta:
        model = models.StoreSales
        fields = [
            'user','prodid', 'storeid', 'pub_date', 'units_sold'
        ]


# class UpdateSalesDataForm(forms.ModelForm):
#     user = forms.CharField()
#     entry = forms.IntegerField()
#     prod_id = forms.CharField()
#     store_id = forms.CharField()
#     pub_date = forms.DateTimeField(
#         widget=DatePickerInput
#     )
#     units_sold = forms.IntegerField()

#     class Meta:
#         model = models.StoreSales
#         fields = [
#             'user', 'entry', 'prod_id', 'store_id', 'pub_date', 'units_sold'
#         ]