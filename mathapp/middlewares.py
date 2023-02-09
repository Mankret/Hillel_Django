from mathapp.models import LogModel


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if '/admin/' not in request.path:
            if request.method == 'POST':
                LogModel.objects.create(path=request.path,
                                        method=request.method,
                                        body=request.POST.dict(),
                                        query=request.GET.dict(),
                                        user=request.user.username,
                                        )
            LogModel.objects.create(path=request.path,
                                    method=request.method,
                                    query=request.GET.dict(),
                                    user=request.user.username)
        return response
