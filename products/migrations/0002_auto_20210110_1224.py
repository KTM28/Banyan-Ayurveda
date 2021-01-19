# Generated by Django 3.1.3 on 2021-01-10 12:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='benefit',
            field=ckeditor.fields.RichTextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=900),
        ),
    ]