import requests
from django.conf import settings


def initiate_payment(data):
    store_id = settings.SSLCOMMERZ['store_id']
    store_pass = settings.SSLCOMMERZ['store_pass']
    sandbox = settings.SSLCOMMERZ['sandbox']

    url = 'https://sandbox.sslcommerz.com/gwprocess/v4/api.php' if sandbox else 'https://securepay.sslcommerz.com/gwprocess/v4/api.php'

    post_data = {
        'store_id': store_id,
        'store_passwd': store_pass,
        'total_amount': data['amount'],
        'currency': 'BDT',
        'tran_id': data['tran_id'],
        'success_url': data['success_url'],
        'fail_url': data['fail_url'],
        'cancel_url': data['cancel_url'],
        'cus_name': data['cus_name'],
        'cus_email': data['cus_email'],
        'cus_phone': data['cus_phone'],
        'cus_add1': data['cus_address'],
        'cus_city': data['cus_city'],
        'cus_country': data['cus_country'],
        'shipping_method': 'NO',
        'product_name': data['product_name'],
        'product_category': 'Ecommerce',
        'product_profile': 'general',
    }

    response = requests.post(url, data=post_data)
    return response.json()
