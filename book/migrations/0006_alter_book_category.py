# Generated by Django 4.1.6 on 2023-02-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_thumbnail_delete_createreviewview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('manga', '漫画'), ('fan', '推し'), ('other', 'その他')], max_length=100),
        ),
    ]
