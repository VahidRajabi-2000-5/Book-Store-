# Generated by Django 5.1.6 on 2025-02-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='book_covers/'),
        ),
    ]
