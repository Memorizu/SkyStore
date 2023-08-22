
from product.models import Product
from django import forms


banned_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_published':
                field.widget.attrs['class'] = None
            if field_name == 'category':
                field.help_text = 'Выберите категорию'
            
                
              
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput,
        }

    def clean_field(self, field_name):
        cleaned_data = self.cleaned_data.get(field_name)
        
        if cleaned_data in banned_list:
            raise forms.ValidationError(f'Были использованы запрещенные слова в {field_name}.')
            
        return cleaned_data

    def clean_name(self):
        return self.clean_field('name')
        
    def clean_description(self):
        return self.clean_field('description')
        

class ModeratorProductForm(ProductForm):
    
    class Meta:
        model = Product
        fields = ['description', 'category', 'is_published']
