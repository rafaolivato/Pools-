# Generated by Django 4.2.8 on 2024-01-05 17:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=200),
        ),
    ]
