# Generated by Django 2.2.3 on 2019-10-06 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_delete_justimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='JustImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theoneimage', models.ImageField(blank=True, default='img', upload_to='products/%Y/%m/%d')),
                ('name', models.CharField(blank=True, db_index=True, default='imgname', max_length=200)),
                ('slug', models.SlugField(blank=True, default='imgslug', max_length=200, unique=True)),
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
        ),
    ]
