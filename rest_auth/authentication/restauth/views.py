from django.shortcuts import render
from rest_framework.response import Response
from .models import Person
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



# Create your views here.
def success_response(response, status_code=None):
    json_obj = {
        "hasError": False,
        "errorCode": -1,
        "message": "Success",

    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status=status_code)


def failure_response(response, status_code=None, error_code=1001, message="Failure"):
    json_obj = {
        "hasError": True,
        "errorCode": error_code,
        "message": message,

    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status_code)


class AddUser(APIView):
    def post(self, request):
        data = {}
        response = {}

        try:
            # Assuming you have a User model defined in your app
            p = User()
            person = Person()

            p.first_name = request.data.get('firstname')
            p.last_name = request.data.get('lastname')
            p.username = request.data.get('username')
            p.email = request.data.get('email')
            password = request.data['password']
            p.set_password(password)
            p.save()

            person.name = request.data.get('name')
            person.age = request.data.get('age')
            person.gender = request.data.get('gender')
            person.username = request.data.get('username')
            person.status = 1
            person.save()

            data = {
                'firstname': p.first_name,
                'last_name': p.last_name,
                'username': p.username,
                'email': p.email,
                'password': password,
                'name': person.username,
                'age': person.age,
                'gender': person.gender,
                'status':person.status
            }

            response = {
                "isSuccess": True,
                'statusMessage': 'Successfully done',
                'data': data
            }

            return success_response(response)

        except Exception as e:
            response['statusMessage'] = 'Wrong data'
            return failure_response(response)

class auth_login(APIView):
    def post(self, request):
        data = {}
        response = {}

        try:
            userName = request.data['username']
            password = request.data['password']

            p = authenticate(username=userName, password=password)

            if p is not None:
                person = Person.objects.get(username=p)

                data = {
                    'firstname': p.first_name,
                    'last_name': p.last_name,
                    'username': p.username,
                    'email': p.email,
                    'password': password,
                    'name': person.username,
                    'age': person.age,
                    'gender': person.gender,
                    'status': person.status
                }
            else:
                response['statusMessage'] = 'User not found'
                return failure_response(response)

        except Exception as e:
            response['statusMessage'] = 'wrong entris'
            return failure_response(response)


        response["isSuccess"] = True
        response['statusMessage'] = 'succesffully done'
        response['data'] = data
        return success_response(response)

