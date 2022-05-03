from django.http import HttpResponseNotFound
from django.utils.deprecation import MiddlewareMixin


class AuthVerify(MiddlewareMixin):
    def process_request(self, request):
        info_dict = request.session.get('info')
        # 如果拿到登录信息 说明已经登录了，则return 往后执行
        if info_dict:
            return
        # 没有登录 返回状态码 前端拿到后跳转到登录页面
        return HttpResponseNotFound("Fucking!")

    def process_response(self, request, response):
        print('AuthVerify 离开了')
        return response
