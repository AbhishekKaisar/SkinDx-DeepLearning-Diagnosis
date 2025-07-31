from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import User

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user_data = sociallogin.account.extra_data
        google_uid = sociallogin.account.uid
        email = user_data.get('email')
        name = user_data.get('name', '')
        picture = user_data.get('picture', '')

        if not email:
            raise ValueError("Email is required")

        try:
            # Try to find existing user by UID
            user = User.objects.get(google_uid=google_uid)
        except User.DoesNotExist:
            try:
                # Fallback: try to find by email
                user = User.objects.get(email=email)
                user.google_uid = google_uid
            except User.DoesNotExist:
                # New user
                user = User(
                    name=name,
                    email=email,
                    google_uid=google_uid,
                    profile_image=picture,
                    trial_credits=3,
                )
        user.save(using='default')  # using MySQL db
        sociallogin.user = user
        return user