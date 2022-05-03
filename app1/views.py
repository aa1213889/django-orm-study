import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app1.models import UserInfo
from app1.utils import password_encrypt


# Create your views here.


def index(request):
    return HttpResponse('<h1>123</h1>')


def user_list(request):
    return render(request, 'user_list.html')


def something(request):
    # request是一个对象，封装了客户端发送过来的所有请求数据

    # 1.获取请求方式 GET/POST
    print(request.method)

    # 2.获取URL传递的值
    print(request.GET)

    # 3.获取POST传递的值
    print(request.POST)

    # 4.[响应] 返回内容
    return HttpResponse({
        'name': '123'
    })

    # 5.[响应] 返回HTML模版
    # return render("hello")

    # 6.[响应] 地址重定向
    # return redirect("https://wwww.baidu.com")


def test_orm(request):
    UserInfo.objects.all().update(password=999)
    UserInfo.objects.filter(name="jz").update(age=20)

    return HttpResponse('OK')


def klw_api(request):

    data_list = list(UserInfo.objects.all().values('name', 'age', 'email', 'size'))
    response_data = {
        'code': 200,
        'msg': data_list
    }
    return JsonResponse(response_data)


def klw_order_api(request):

    data_list = list(UserInfo.objects.all().values('name', 'age', 'email', 'size'))

    response_data = {
        'code': 200,
        'msg': data_list
    }
    return JsonResponse(response_data)


def add_user(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode('utf8'))
        print(type(params))
        UserInfo.objects.create(
            age=params.get("age"),
            name=params['name'],
            email=params['mail'],
            size=params['size'],
            password=password_encrypt(params['pwd'])
        )
        return JsonResponse({
            'code': 200,
            'msg': '添加成功'
        })


def login_user(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode('utf8'))
        user_obj = UserInfo.objects.filter(name=params['name'], password=password_encrypt(params['pwd'])).first()
        if user_obj == None:
            return JsonResponse({
                'code': 403,
                'msg': '登录失败'
            })

        # 帐号密码正确后，将用户信息写入session
        request.session['info'] = {'id': user_obj.id, 'name': user_obj.name}
        return JsonResponse({
            'code': 200,
            'msg': '登录成功'
        })


def logout_user(request):
    request.session.clear()
    return JsonResponse({
        'code': 403,
        'msg': '退出成功'
    })
