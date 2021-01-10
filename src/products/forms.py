from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'description', 'sku',
                'category', 'price',
                'rating',
                'image_url',
                'image',
                'discontinued',
                )
    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Product Name *',
            'description': 'Write Your Product Description here *',
            'sku': 'SKU *',
            'category': 'Category *',
            'image_url': 'Image URL (optional)',
            'image': 'Image',
            'price': 'Price € *',
            'rating': 'Rating 0-5',
            'discontinued': 'Discontinued',
        }
    
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field in self.fields:
            self.fields[field].label = labels[field]
        
        self.fields['description'].widget.attrs['rows'] = 4
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['price'].widget.attrs['max'] = 1000
        self.fields['rating'].widget.attrs['min'] = 0
        self.fields['rating'].widget.attrs['max'] = 5
        