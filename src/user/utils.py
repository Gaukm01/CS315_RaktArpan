from .models import User
import bcrypt

# check if user is already logged in or not
def IsLoggedIn(request):
    if request.session.has_key("username"):
        try:
            # query to check the user with username = current logged in username 
            user = User.objects.get(username=request.session["username"])
            return user
        except:
            return None
    else:
        return None