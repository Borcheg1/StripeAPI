import stripe
from django.shortcuts import get_object_or_404, HttpResponse, render
from django.template import loader
from django.conf import settings
from django.http.response import JsonResponse

from .models import Item


def lists(request):
    items = Item.objects.all()
    template = loader.get_template('form/items.html')
    context = {'items': items}
    return HttpResponse(template.render(context, request))


def detail(request, id):
    data = get_object_or_404(Item, id=id)
    key = settings.STRIPE_PUB_KEY
    template = loader.get_template('form/detail.html')
    context = {'item': data, 'key': key}
    return HttpResponse(template.render(context, request))


def create_checkout_session(request, id):
    data = get_object_or_404(Item, id=id)
    if request.method == "GET":
        url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            session = stripe.checkout.Session.create(
                success_url=url + 'success/',
                cancel_url=url + 'cancelled/',
                mode='payment',
                line_items=[{
                    'price_data': {
                        'currency': 'rub',
                        'product_data': {
                            'name': data.name,
                        },
                        'unit_amount': int(data.price * 100),
                    },
                    'quantity': 1,
                }]
            )
            return JsonResponse({'id': session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def success(request):
    return render(request, 'form/success.html')


def cancelled(request):
    return render(request, 'form/cancelled.html')
