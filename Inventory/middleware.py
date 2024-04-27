from typing import Any


class Prueba():
    def __init__(self,get_response) :
        self.get_response = get_response
    

    def __call__(self, request):
        
        
        response = self.get_response(request)


        return response


    def process_view(self,request,view_func,view_args,view_kwargs): #function that activate before the view and response and after 
                                                                    #the view and response
        if 'anonymoususer' == str(request.user).lower():
            print('HEY ANON')
            print(request.META.get('PATH_INFO'))
        else:
            print(request.user)
            print(request.META.get('PATH_INFO'))
