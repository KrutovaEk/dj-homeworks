# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from flask import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorChangeSerializer


# class SensorView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorDetailSerializer(sensors, many=True)
#         return Response(ser.data)
#
# class MeasurementView(APIView):
#     def get(self, request):
#         measurement = Measurement.objects.all()
#         ser = MeasurementSerializer(measurement, many=True)
#         return Response(ser.data)

class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorChangeView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


