from django import  forms
from students.models import product,Category,User



class productForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    current_price = forms.IntegerField(label="Price", required=False)
    description = forms.charField(label="Description", max_length=200, required=False)
    image = forms.ImageField(label="image", required=False)
    email = forms.EmailField(label="email", max_length=200, required=False)
    product_id = forms.ModelChoiceField(queryset=product.objects.all(), label="Category", required=False)
    def clean_email(self):
        email = self.cleaned_data['email']
        # check if email exists in students --> data not valid
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists before")
        return email

class productModelForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','current_price','description','image'.'email' ,'product_id']

    def clean_email(self):
        email = self.cleaned_data['email']

        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists before")

        return email

class UserForm(forms.ModelForm):
    class Meta:
        model = User
         fields = ['user', 'email','password']
