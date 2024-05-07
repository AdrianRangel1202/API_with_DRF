from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status, authentication, exceptions
from apps.users.authentication import ExpiringTokenAuthentication





class Authentication(authentication.BaseAuthentication):
    user = None


    def get_user(self, request):
        """
        Obtiene el token del header.

        revisa su tiempo de expiracion y regresa el usuario sino 
        regresa un None

        """
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)

            if user != None:
                self.user = user
                return user

        return print(user)
    
    def authenticate(self, request):  

        """
        return:
            request.user = self.user
            request.auth = None
        """

        if self.get_user(request) is None:
            raise exceptions.AuthenticationFailed('No se han enviado las credenciales correctamente!!.')
        
        return (self.user, None)
