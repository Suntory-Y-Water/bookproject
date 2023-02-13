# Generated by Django 4.1.6 on 2023-02-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_delete_samplemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('manga', '漫画'), ('other', 'その他')], max_length=100),
        ),
    ]
