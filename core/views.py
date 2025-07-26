from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import uuid
from sslcommerz.utils.sslcommerz import initiate_payment


def home(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'login.html')


@login_required
def test_skin(request):
    trial_used = request.session.get('trial_count', 0)

    if trial_used >= 3:
        return redirect('trial_ends')

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        request.session['trial_count'] = trial_used + 1

        prediction = "Melanoma"
        confidence = "94%"

        return render(request, 'test_skin.html', {
            'prediction': {
                'label': prediction,
                'confidence': confidence,
                'image': image_url,
            }
        })

    return render(request, 'test_skin.html')


@login_required
def trial_ends(request):
    if request.method == 'POST':
        tran_id = str(uuid.uuid4())
        data = {
            'amount': '33.79',
            'tran_id': tran_id,
            'success_url': request.build_absolute_uri('/payment/success/'),
            'fail_url': request.build_absolute_uri('/payment/fail/'),
            'cancel_url': request.build_absolute_uri('/payment/cancel/'),
            'cus_name': request.user.get_full_name(),
            'cus_email': request.user.email,
            'cus_phone': '01234567890',  # Placeholder
            'cus_address': 'N/A',  # Placeholder
            'cus_city': 'N/A',  # Placeholder
            'cus_country': 'N/A',  # Placeholder
            'product_name': 'SkinDx Subscription',
        }

        response = initiate_payment(data)

        if response.get('status') == 'SUCCESS':
            return redirect(response['GatewayPageURL'])
        else:
            return render(request, 'payment/error.html', {'error': response})

    return render(request, 'trial_ends.html')


def logout_view(request):
    logout(request)
    return redirect('home')