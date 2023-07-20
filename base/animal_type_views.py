from django.http import HttpResponseNotAllowed, JsonResponse
from base.models import AnimalType


def animal_type_list_endpoint(request):
    methods = {
        'GET': animal_type_list,
        'POST': animal_type_create
    }
    if request.method in methods.keys():
        return methods[request.method](request)
    else:
        return HttpResponseNotAllowed(permitted_methods=methods.keys())


def animal_type_detail_endpoint(request, pk):
    methods = {
        'GET': animal_type_detail,
        'PUT': animal_type_update,
        'DELETE': animal_type_delete
    }
    if request.method in methods.keys():
        return methods[request.method](request, pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=methods.keys())


def animal_type_list(request):
    animal_types = AnimalType.objects.all().values()
    return JsonResponse(list(animal_types), safe=False)


def animal_type_create(request):
    pass


def animal_type_detail(request, pk):
    try:
        animal_type = AnimalType.objects.filter(pk=pk).values().first()
        if animal_type:
            return JsonResponse(animal_type, safe=False)
        else:
            return JsonResponse({'error': 'AnimalType not found'}, status=404)
    except ValueError:
        return JsonResponse({'error': 'Invalid value for the primary key'}, status=400)


def animal_type_update(request, pk):
    pass


def animal_type_delete(request, pk):
    pass
