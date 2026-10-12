from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .forms import ProviderRegistrationForm, BookingForm
from .models import Provider, Booking


# =========================
# PROVIDER REGISTRATION
# =========================

@ensure_csrf_cookie
def register(request):

    if request.method == "POST":

        form = ProviderRegistrationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            provider = form.save()

            if request.headers.get("X-Requested-With") == "XMLHttpRequest":

                return JsonResponse({
                    "success": True,
                    "message": "Application submitted successfully.",
                    "provider_id": provider.id,
                    "status": provider.status
                })

            return render(
                request,
                "providers/success.html",
                {
                    "provider": provider
                }
            )

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":

            return JsonResponse({
                "success": False,
                "errors": form.errors.get_json_data()
            }, status=400)

    else:

        form = ProviderRegistrationForm()

    return render(
        request,
        "providers/register.html",
        {
            "form": form
        }
    )


# =========================
# BOOKING
# =========================

@csrf_exempt
def booking(request):

    # =========================
    # GET REQUEST
    # =========================

    if request.method == "GET":

        return JsonResponse({
            "success": True,
            "message": "Booking endpoint is working."
        })


    # =========================
    # POST REQUEST
    # =========================

    if request.method == "POST":

        print("========== BOOKING POST ==========")
        print("POST DATA:", request.POST)

        form = BookingForm(request.POST)

        print("FORM VALID:", form.is_valid())
        print("FORM ERRORS:", form.errors)


        # =========================
        # VALID FORM
        # =========================

        if form.is_valid():

            booking_obj = form.save()

            print("BOOKING SAVED:", booking_obj.id)

            return JsonResponse({
                "success": True,
                "booking_id": booking_obj.id,
                "client_name": booking_obj.client_name,
                "service": booking_obj.service,
                "message": "Booking submitted successfully."
            })


        # =========================
        # INVALID FORM
        # =========================

        return JsonResponse({
            "success": False,
            "errors": form.errors.get_json_data()
        }, status=400)


    # =========================
    # INVALID REQUEST
    # =========================

    return JsonResponse({
        "success": False,
        "message": "Invalid request."
    }, status=400)


# =========================
# VERIFIED PROVIDERS
# =========================

def providers(request):

    qs = Provider.objects.filter(
        status="approved"
    ).select_related("user")

    service = request.GET.get("service")

    if service:

        qs = qs.filter(
            service=service
        )

    return render(
        request,
        "providers/providers.html",
        {
            "providers": qs,
            "service": service
        }
    )


# =========================
# PROVIDER DETAIL
# =========================

def detail(request, pk):

    provider = get_object_or_404(
        Provider,
        pk=pk,
        status="approved"
    )

    return render(
        request,
        "providers/detail.html",
        {
            "provider": provider
        }
    )