from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        return render(request, 'payment/success.html', {'data': request.POST})
    return redirect('/')


@csrf_exempt
def payment_fail(request):
    return render(request, 'payment/fail.html')


@csrf_exempt
def payment_cancel(request):
    return render(request, 'payment/cancel.html')