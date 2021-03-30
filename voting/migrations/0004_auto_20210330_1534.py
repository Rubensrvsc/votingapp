# Generated by Django 3.1.4 on 2021-03-30 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20210330_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleitor',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='nome',
        ),
        migrations.AddField(
            model_name='vote',
            name='eleitor_vote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eleitor_vote', to='voting.eleitor'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=300)),
                ('itens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eleitor_item', to='voting.eleitor')),
            ],
        ),
        migrations.AddField(
            model_name='vote',
            name='item_vote',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_vote', to='voting.item'),
        ),
    ]