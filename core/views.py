from core.models import PhotoUpload, User
from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import uuid
from core.sslcommerz.utils import initiate_payment
from django.views.decorators.csrf import csrf_exempt
from allauth.socialaccount.models import SocialAccount


def home(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'login.html')


@login_required
def test_skin(request):
    try:
        social = SocialAccount.objects.get(user=request.user, provider='google')
        google_uid = social.extra_data.get('sub')
        custom_user = User.objects.get(google_uid=google_uid)
        if custom_user.trial_credits <= 0:
            return redirect('trial_ends')
    except Exception:
        return redirect('trial_ends')

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        # Save image info to PhotoUpload table
        user = request.user
        try:
            social = SocialAccount.objects.get(user=user, provider='google')
            google_uid = social.extra_data.get('sub')
            custom_user = User.objects.get(google_uid=google_uid)
            upload = PhotoUpload.objects.create(
                user_id=custom_user.user_id,
                image_url=image_url,
                uploaded_at=now()
            )
            from core.models import TestResult
            from decimal import Decimal
            prediction = "Melanoma"
            confidence = Decimal("0.94")
            TestResult.objects.create(
                upload_id=upload.upload_id,
                disease_name=prediction,
                confidence=confidence,
                tested_at=now()
            )

            # Decrease trial credits
            if custom_user.trial_credits > 0:
                custom_user.trial_credits -= 1
                custom_user.save()

        except User.DoesNotExist:
            print("⚠️ User not found in custom User table.")
        except SocialAccount.DoesNotExist:
            print("⚠️ SocialAccount not found.")

        return render(request, 'test_skin.html', {
            'prediction': {
                'label': prediction,
                'confidence': confidence,
                'image': image_url,
            },
            'trial_credits': custom_user.trial_credits
        })

    try:
        social = SocialAccount.objects.get(user=request.user, provider='google')
        google_uid = social.extra_data.get('sub')
        custom_user = User.objects.get(google_uid=google_uid)
        trial_credits = custom_user.trial_credits
    except Exception:
        trial_credits = 0
    return render(request, 'test_skin.html', {
        'trial_credits': trial_credits
    })


@login_required
def trial_ends(request):
    if request.method == 'POST':
        tran_id = str(uuid.uuid4())
        try:
            social = SocialAccount.objects.get(user=request.user, provider='google')
            google_uid = social.extra_data.get('sub')
            custom_user = User.objects.get(google_uid=google_uid)
            from core.models import Payment
            Payment.objects.create(
                user_id=custom_user.user_id,
                transaction_id=tran_id,
                amount=33.79,
                payment_method='bkash',
                payment_status='pending'
            )
        except Exception as e:
            print("⚠️ Failed to create payment record:", e)

        data = {
            'amount': '33.79',
            'tran_id': tran_id,
            'success_url': request.build_absolute_uri('/payment/success/'),
            'fail_url': request.build_absolute_uri('/payment/fail/'),
            'cancel_url': request.build_absolute_uri('/payment/cancel/'),

            # ✅ Customer info
            'cus_name': request.user.get_full_name() or 'Unknown User',
            'cus_email': request.user.email or 'demo@email.com',
            'cus_phone': '01234567890',
            'cus_add1': 'N/A',
            'cus_city': 'Dhaka',
            'cus_country': 'Bangladesh',

            # ✅ Product info
            'product_name': 'SkinDx Subscription',
            'shipping_method': 'NO',
            'product_category': 'Electronic',
            'product_profile': 'general',

            # ✅ Required shipping info even if shipping_method='NO'
            'shipping_method': 'NO',
            'num_of_item': 1,
            'ship_name': request.user.get_full_name() or 'Unknown User',
            'ship_add1': 'N/A',
            'ship_city': 'Dhaka',
            'ship_country': 'Bangladesh',
        }

        response = initiate_payment(data)

        if response.get('status') == 'SUCCESS':
            return redirect(response['GatewayPageURL'])
        else:
            return render(request, 'payment/error.html', {'error': response})

    return render(request, 'trial_ends.html')


@csrf_exempt
def payment_success(request):
    from core.models import Payment
    try:
        tran_id = request.POST.get('tran_id') or request.GET.get('tran_id')
        payment = Payment.objects.get(transaction_id=tran_id)
        payment.payment_status = 'completed'
        payment.paid_at = now()
        payment.save()

        user = payment.user
        user.trial_credits += 5
        user.save()

        return HttpResponse("✅ Payment successful! Thank you for subscribing to SkinDx.")
    except Payment.DoesNotExist:
        return HttpResponse("⚠️ Payment record not found.")
    except Exception as e:
        return HttpResponse(f"❌ Payment update failed: {e}")


@csrf_exempt
def payment_fail(request):
    return HttpResponse("❌ Payment failed. Please try again or contact support.")


@csrf_exempt
def payment_cancel(request):
    return HttpResponse("⚠️ Payment was cancelled.")


def logout_view(request):
    logout(request)
    return redirect('home')