from typing import Any
from CortexBack.controller.CortexManager import CortexManager
from CortexBack.utils.tools import api_action
from django.db import models
from CortexPackage.src.main_lib.iNeuralNetwork import INeuralNetwork, Position
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
 
from django.db.models.signals import post_save
from django.dispatch import receiver

class HDF5(models.Model):
    data = models.BinaryField()  # Binaries
    state = models.TextField()
    allowed_methods = ['get']


class TFLayerTypeOption(models.Model):
    name = models.TextField(default=None)
    type = models.TextField()
    possible_values = models.JSONField()

class TFLayerType(models.Model):
    name = models.TextField() 
    options = models.ManyToManyField(to=TFLayerTypeOption, blank=True)

class TFOption(models.Model):
    option = models.OneToOneField(TFLayerTypeOption, on_delete=models.CASCADE)
    option_name = models.TextField()

class Layer(models.Model):
    name = models.TextField()
    type = models.OneToOneField(TFLayerType, null=True, on_delete=models.CASCADE)
    options = models.ManyToManyField(TFOption, blank=True)

class NeuralNetwork(models.Model):
    hdf5 = models.ForeignKey(HDF5, null=True, on_delete=models.CASCADE)
    # input_shape = models.JSONField()  # int table

    name = models.TextField()
    layers = models.ManyToManyField(Layer, blank=True)

class Cortex(models.Model):
    metadata = models.TextField()  # string

    @api_action('predict', 'POST')
    def predict(self, request, pk=None):
        print(request.data)
        CortexManager().neural_net_matrix = list(NeuralNetworkConfig.objects.all())
        data = CortexManager().start(request.data)
        print("prediction")
        # workspace = Workspace.objects.first() # Change this line to get the correct Workspace instance
        # workspace.doAction()
        return Response({"status": "success", "data" : str(data)}, status=status.HTTP_200_OK)
    
class NeuralNetworkConfig(models.Model):
    neural_network = models.OneToOneField(NeuralNetwork, null=True, on_delete=models.CASCADE)  # N:1
    next_neural_network = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='link_next_neural_network')  # N:N
    previous_neural_network = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='link_previous_neural_network')  # N:N
    cortex = models.ForeignKey(Cortex, default=None, on_delete=models.CASCADE)
    nn_position = models.IntegerField(default=1, choices=Position.format())

    def get_next_ids(self):
        return [nn.id for nn in self.next_neural_network.all()]
    
    def get_previous_ids(self):
        return [nn.id for nn in self.previous_neural_network.all()]

class Workspace(models.Model):
    cortex = models.OneToOneField(Cortex, on_delete=models.CASCADE)

    @api_action('do_action', 'POST')
    def do_action(self, request, pk=None):
        print("test")
        # workspace = Workspace.objects.first() # Change this line to get the correct Workspace instance
        # workspace.doAction()
        return Response({"status": "success"}, status=status.HTTP_200_OK)

