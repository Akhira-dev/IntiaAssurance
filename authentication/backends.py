from django.contrib.auth.backends import BaseBackend
from authentication.models import Client  # Remplace par l'emplacement réel de ton modèle utilisateur

class CustomBackendSystem(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Client.objects.get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except Client.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        """Vérifie si l'utilisateur est actif."""
        return getattr(user, 'is_active', False)
