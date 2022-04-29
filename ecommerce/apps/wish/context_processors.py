from .models import Wish


def wish_list(request):
    if request.user.is_anonymous:
        return {}
    return {
        'wish_list': Wish.objects.filter(user=request.user).select_related('product')
    }
