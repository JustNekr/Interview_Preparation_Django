from .models import HitCount


def hit_count_middleware(get_response):

    def middleware(request):
        try:
            hc, create = HitCount.objects.get_or_create(path=request.path)
            if not create:
                hc.hits += 1
            hc.save()
        except:
            pass
        response = get_response(request)
        return response

    return middleware