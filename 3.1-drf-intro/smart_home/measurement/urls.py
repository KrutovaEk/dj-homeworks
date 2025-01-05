from django.urls import path

# from measurement.views import SensorAPIUpdate

# from measurement.views import SensorView

from measurement.views import SensorListView, MeasurementView, SensorChangeView, SensorView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('measurement/', MeasurementView.as_view()),
    path('sensors/update/<pk>/', SensorChangeView.as_view()),
    path('sensors/<pk>/', SensorView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
