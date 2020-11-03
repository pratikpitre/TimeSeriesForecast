from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Predict
from .serializers import predictSerializers
#import numpy as np 
import pandas as pd
from keras.models import load_model
from numpy import array
from rest_framework.views import APIView

# Create your views here.
'''
class PredictionsView:
    queryset = predict.objects.all()
    serializer_class = predictSerializer
'''


class Predictions(APIView):
    def post(self, request):
        try:
            model = load_model('/Users/admin/Home/DRFBasedAPIForLSTM/LSTM_20201102.h5')
            
            request_data = request.data
            x_input = array(list(request_data.values()))
            x_input = x_input.reshape((1, 3, 1))
            yhat = model.predict(x_input, verbose=0)
            return JsonResponse('Predicted value of the sequence will be {}'.format(yhat), safe=False)
            #return JsonResponse(x_input, safe=False)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    '''
    def delete(self, request):
        return JsonResponse('GET Request on Predictions', safe=False)        
    '''

class PredictionsView(APIView):
    def get(self, request):
        return JsonResponse('you can get the next sequence with /predictions extention on this url', safe=False)