from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from .models import User
from django.utils.timezone import now

@receiver(user_logged_in)
def save_user_to_mysql(sender, request, user, **kwargs):
    print("✅ Signal fired: user_logged_in")

    try:
        social = SocialAccount.objects.get(user=user, provider='google')
        extra_data = social.extra_data
        google_uid = extra_data.get('sub')
        email = extra_data.get('email') or user.email
        name = extra_data.get('name') or user.get_full_name() or user.username
        picture = extra_data.get('picture')

        print(f"Google UID: {google_uid}")
        print(f"Email: {email}")

        if not User.objects.filter(google_uid=google_uid).exists():
            User.objects.create(
                name=name,
                email=email,
                profile_image=picture,
                google_uid=google_uid,
                trial_credits=3,
                created_at=now(),
                updated_at=now()
            )
            print("✅ User inserted into DB")
        else:
            print("ℹ️ User already exists in DB")

    except Exception as e:
        print(f"❌ User save error: {str(e)}")