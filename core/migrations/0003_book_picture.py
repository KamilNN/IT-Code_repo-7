# Generated by Django 5.0.4 on 2024-05-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book_author_book_description_book_genre_book_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures', verbose_name='Фото обложки'),
        ),
    ]
