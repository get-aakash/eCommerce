# Generated by Django 3.2.4 on 2021-06-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerceApp', '0007_rename_review_userreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='productReview',
            field=models.TextField(),
        ),
    ]
