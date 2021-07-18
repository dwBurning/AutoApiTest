import json

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializers


class Contact():
    def __init__(self):
        self.contacts = []

    def add(self, person):
        if person not in self.contacts:
            self.contacts.append(person)
        else:
            print("exists")

    def get(self, person):
        try:
            pos = self.contacts.index(person)
            return self.contacts[pos]
        except:
            return None

    def get_all(self):
        return self.contacts

    def delete(self, person):
        self.contacts.remove(person)


contact = Contact()

class PersonController(APIView):

    def get(self, request, id=0):
        if id:
            p = Person(id)
            if contact.get(p):
                serializer = PersonSerializers(instance=contact.get(p))
                return JsonResponse({'code': 0, 'message': '获取成功', 'data': serializer.data}, safe=False, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({'code': -1, 'message': '人事资料不存在', 'data': None}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            serializer = PersonSerializers(
                instance=contact.get_all(), many=True)
            return JsonResponse({'code': 0, 'message': '获取成功', 'data': serializer.data}, safe=False, json_dumps_params={'ensure_ascii': False})

    def delete(self, request, id=0):
        p = Person(id)
        if contact.get(p):
            contact.delete(p)
            return JsonResponse({'code': 0, 'message': '删除成功', 'data': None}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'code': -1, 'message': '人事资料不存在', 'data': None}, safe=False, json_dumps_params={'ensure_ascii': False})

    def patch(self, request, id):
        data = json.loads(request.body)
        p = contact.get(Person(id))
        if p:
            for key, value in data.items():
                setattr(p, key, value)
            return JsonResponse({'code': 0, 'message': '修改成功', 'data': None}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'code': -1, 'message': '人事资料不存在', 'data': None}, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        data = json.loads(request.body)
        p = Person()
        for key, value in data.items():
                setattr(p, key, value)
        person = contact.get(p)
        if person:
            return JsonResponse({'code': -1, 'message': '人事资料已存在', 'data': None}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            contact.add(p)
            return JsonResponse({'code': 0, 'message': '添加成功', 'data': None}, safe=False, json_dumps_params={'ensure_ascii': False})
