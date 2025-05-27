import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Item

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    key = settings.STRIPE_KEYS[item.currency]['publishable']
    return render(request, 'item.html', {'item': item, 'stripe_key': key})

def create_checkout_session(request, item_id):
    item = Item.objects.get(id=item_id)
    stripe.api_key = settings.STRIPE_KEYS[item.currency]['secret']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=settings.SUCCESS_URL,
        cancel_url=settings.CANCEL_URL,
    )
    return JsonResponse({'id': session.id})

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')