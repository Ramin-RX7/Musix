from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend



class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        login_type = "username"
        if username is None:
            # username = kwargs.get(UserModel.USERNAME_FIELD)
            login_type = "email"
        if username is None or password is None:
            return
        try:
            if login_type == "username":
                user =  UserModel.objects.get(username=username)
            else:
                user =  UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user