from django.shortcuts import render
from common.json import ModelEncoder
from .models import Shoe, BinVO
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse


# Create your views here.
class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "bin_number",
        "bin_size",
        "import_href",
    ]



class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
    ]

    encoders = {"bin": BinVOEncoder()}


class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "id",
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
    ]

    encoders = {"bin": BinVOEncoder()}


@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        print(f"{shoes}")
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            bin_href = content["bin"]
            bin = BinVO.objects.get(import_href=bin_href)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeListEncoder,
            safe=False
        )


@require_http_methods(["GET", "PUT", "DELETE"])
def api_detail_shoes(request, pk):
    if request.method == "GET":
        try:
            shoe = Shoe.objects.get(id=pk)
            return JsonResponse(
                {"shoe": shoe},
                encoder=ShoeDetailEncoder,
                safe=False
            )
        except Shoe.DoesNotExist:
            return JsonResponse(
                {"message": "Shoe Does Not Exist"},
                status=400,
            )
    elif request.method == "PUT":
        content = json.loads(request.body)
        try:
            if "bin" in content:
                bin_href = content["bin"]
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "BinVO does not exist"},
                status=400,
            )
        Shoe.objects.filter(id=pk).update(**content)
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )
    else:
        count, _ = Shoe.objects.filter(id=pk).delete()
        return JsonResponse({"Shoe deleted": count > 0})
