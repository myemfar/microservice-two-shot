from django.views.decorators.http import require_http_methods
from .models import LocationVO, Hat
from common.json import ModelEncoder
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.


class LocationVOEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "closet_name",
        "import_href"
    ]

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture",
        "location",
        "id"
    ]
    encoders = {
        "location": LocationVOEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
        {"hats": hats},
        encoder=HatDetailEncoder,
        safe=False,
        )
    else:
        content = json.loads(request.body)
        try:
            location_href = content["location"]
            location = LocationVO.objects.get(import_href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location href"},
                status=400,
            )
        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )


@require_http_methods(["GET", "PUT", "DELETE"])
def api_hat_detail(request, hat_id):
    try:
        hat = Hat.objects.get(id=hat_id)
    except Hat.DoesNotExist:
        return JsonResponse({"message": "404 Hat not found"})
    if request.method == "GET":
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
    elif request.method == "PUT":
        try:
            content = json.loads(request.body)
        except json.JSONDecodeError:
            response = JsonResponse({"message": "Bad JSON"})
            response.status_code = 400
            return response
        try:
            location_href = content["location"]
            location = LocationVO.objects.get(import_href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location href"},
                status=400,
            )
        hat = Hat.objects.update(**content)
        hat = Hat.objects.filter(id=hat_id)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False
        )
    else:
        try:
            hat = Hat.objects.get(id=hat_id)
            hat.delete()
            return JsonResponse({"message": "hat deleted successfully"})
        except Hat.DoesNotExist:
            return JsonResponse({"message": "hat does not exist"})
