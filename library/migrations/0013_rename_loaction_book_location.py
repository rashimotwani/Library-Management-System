# Generated by Django 4.0.4 on 2022-07-14 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_book_loaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='loaction',
            new_name='location',
        ),
    ]
