from mathapp.models import LogModel


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if '/admin/' in request.path:
            return response
        LogModel.objects.create(path=request.path,
                                method=request.method,
                                body=request.POST.dict(),
                                query=request.GET.dict(),
                                user=request.user.username,
                                )

        return response
