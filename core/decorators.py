from django.http import HttpResponse


def group_required(groups=[]):
    groups_set = set(groups)

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user_groups = set([group.name for group in request.user.groups.all()])
            if user_groups.intersection(groups_set) or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Not authorised')

        return wrapper

    return decorator
