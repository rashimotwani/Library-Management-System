# Generated by Django 4.0.4 on 2022-07-07 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_book_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookCopies',
        ),
    ]
