# Generated by Django 4.1.6 on 2023-02-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_review_createreviewview'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='CreateReviewView',
        ),
    ]