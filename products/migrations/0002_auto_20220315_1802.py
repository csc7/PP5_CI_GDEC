# Generated by Django 3.2 on 2022-03-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='resolution',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]