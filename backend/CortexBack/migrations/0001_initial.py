# Generated by Django 4.2.6 on 2023-10-12 08:34

import CortexPackage.src.main_lib.iNeuralNetwork
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cortex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HDF5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.BinaryField()),
                ('state', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NeuralNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('hdf5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CortexBack.hdf5')),
                ('layers', models.ManyToManyField(blank=True, to='CortexBack.layer')),
            ],
        ),
        migrations.CreateModel(
            name='TFLayerTypeOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=None)),
                ('type', models.TextField()),
                ('possible_values', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cortex', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CortexBack.cortex')),
            ],
        ),
        migrations.CreateModel(
            name='TFOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.TextField()),
                ('option', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CortexBack.tflayertypeoption')),
            ],
        ),
        migrations.CreateModel(
            name='TFLayerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('options', models.ManyToManyField(blank=True, to='CortexBack.tflayertypeoption')),
            ],
        ),
        migrations.CreateModel(
            name='NeuralNetworkConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nn_position', models.IntegerField(choices=[(0, 'FIRST'), (1, 'MIDDLE'), (2, 'LAST')], default=1)),
                ('cortex', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CortexBack.cortex')),
                ('neural_network', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CortexBack.neuralnetwork')),
                ('next_neural_network', models.ManyToManyField(blank=True, to='CortexBack.neuralnetworkconfig')),
                ('previous_neural_network', models.ManyToManyField(blank=True, to='CortexBack.neuralnetworkconfig')),
            ],
            bases=(models.Model, CortexPackage.src.main_lib.iNeuralNetwork.INeuralNetwork),
        ),
        migrations.AddField(
            model_name='layer',
            name='options',
            field=models.ManyToManyField(blank=True, to='CortexBack.tfoption'),
        ),
        migrations.AddField(
            model_name='layer',
            name='type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CortexBack.tflayertype'),
        ),
    ]
