from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import CarModel


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        res = [{'id': car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year}for car in cars]
        return Response(res)

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        CarModel.objects.create(**data)
        return Response("created")

    def put(self, *args, **kwargs):
        data = self.request.data
        print(data)
        CarModel.objects.filter(id=data['id']).update(**data)
        return Response("updated")

    def delete(self, *args, **kwargs):
        CarModel.objects.filter(id=kwargs['pk']).delete()


