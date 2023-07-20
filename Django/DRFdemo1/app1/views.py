from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import UserInfo
from .serializers import UserInfoSerializer


# Create your views here.

class UserListView(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass


def user_list(request):
    """
    get方法请求：获取用户列表
    post方法请求：添加用户信息
    :param request:
    :return:
    """
    if request.method == "GET":
        # 获取用户信息列表
        users = UserInfo.objects.all()
        # 创建序列化对象
        ser = UserInfoSerializer(users, many=True)
        result = {
            'data': ser.data,
            'code': 200,
            "message": "OK"
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        a = {"id": 1, "name": "sunliguo", "pwd": "123435", "email": "1234@qq.com", "age": 10
             }
        params = JSONParser().parse(request)
        # 创建序列化器
        ser = UserInfoSerializer(data=params)
        # 校验请求数据
        if ser.is_valid():
            # 校验通过，则添加数据到数据
            ser.save()
            return JsonResponse({'code': 201, 'data': ser.data, "message": 'OK'})
        else:
            return JsonResponse({'code': 400, 'message': ser.errors})

    else:
        return JsonResponse({'code': 405, 'message': f"不支持该请求{request.method}"})


def user_detail(request, id):
    """
    GET:获取单个用户信息
    PUT：修改单个用户信息
    DELETE:删除用户信息
    :param request:
    :param id:
    :return:
    """
    try:
        obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return HttpResponse('404 访问资源不存在', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser = UserInfoSerializer(obj)
        return JsonResponse({'code': 200, "data": ser.data, 'message': "OK"})
    elif request.method == "PUT":
        # 修改单个用户资源

        # ser = UserInfoSerializer(instance=obj, data=json.loads(request.body.decode('utf-8')))

        params = JSONParser().parse(request)
        ser = UserInfoSerializer(instance=obj, data=params)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'code': 200, "data": ser.validated_data, "message": "OK"})
        else:
            return JsonResponse({'code': 400, 'message': ser.errors})
    elif request.method == 'DELETE':
        obj.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'code': 405, 'message': f"不支持该请求{request.method}"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)


class BookView(View):
    def get(self, request):
        return HttpResponse('BookView get run')

    def post(self, request):
        return HttpResponse('BookView post run')

    def delete(self, request):
        return HttpResponse('BookView delete run')


class BookView2(APIView):
    def post(self, request):
        print(type(request.data))
        print(request.data)
        return HttpResponse(f"request.data{request.data}")
