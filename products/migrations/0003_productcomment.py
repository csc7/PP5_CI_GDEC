# Generated by Django 3.2 on 2022-04-12 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0002_auto_20220315_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_rating_value', models.IntegerField(choices=[(5, 'Fantastic'), (4, 'Good'), (3, 'Average'), (2, 'Poor'), (1, 'Very Poor')], default=5)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='profiles.userprofile')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]