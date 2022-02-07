# Generated by Django 4.0.1 on 2022-02-04 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attending', through='levelupapi.EventGamer', to='levelupapi.Gamer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
        migrations.AddField(
            model_name='eventgamer',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.event'),
        ),
        migrations.AddField(
            model_name='eventgamer',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
    ]
