from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from apps.users.authentication import ExpiringTokenAuthentication





class Authentication(object):
    
    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            
            token_expire = ExpiringTokenAuthentication()
            user,token, message, expired = token_expire.authenticate_credentials(token)
            if user != None and token != None:
                return user
            return message
   
        return None

    def dispatch(self, request, *args, **kwargs):
        data = self.get_user(request)
        if data is not None:
            if type(data) == str:
                response = Response({'error':data})
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response
            return super().dispatch(request, *args,**kwargs)
        response = Response({'error':'No se han enviado las credenciales'})
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response