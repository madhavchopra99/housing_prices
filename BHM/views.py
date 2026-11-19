from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import util


def home(request):
    return render(request, "BHM/app.html")


def get_location_names(request):
    response = JsonResponse({"locations": util.get_location_names()})

    return response


@csrf_exempt
def predict_home_price(request):

    if request.method == "POST":
        form = request.POST
        total_sqft = float(form["total_sqft"])
        location = form["location"]
        bhk = int(form["bhk"])
        bath = int(form["bath"])

        response = JsonResponse(
            {
                "estimated_price": util.get_estimated_price(
                    location, total_sqft, bhk, bath
                )
            }
        )
    else:
        return None

    return response
