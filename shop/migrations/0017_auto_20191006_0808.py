# Generated by Django 2.2.3 on 2019-10-06 08:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20191005_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='JustImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theoneimage', models.ImageField(default='img', upload_to='products/%Y/%m/%d')),
                ('name', models.CharField(db_index=True, default='dos', max_length=200)),
                ('slug', models.SlugField(default='uno', max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='info',
            name='justimage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='shop.JustImages'),
            preserve_default=False,
        ),
    ]
