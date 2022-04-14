# Generated by Django 3.2 on 2022-04-12 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0003_productcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofile'),
        ),
    ]