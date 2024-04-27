from typing import Any
import datetime
from datetime import timedelta
from .models import Product

class DueDateMiddleware():
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        response = self.get_response(request)

        return response
    
    def process_view(self,request,view_fun,view_args,view_kwargs):
        if request.user.is_authenticated:
            today = datetime.date.today()
            products = Product.objects.filter(state = True)

            for product in products:
                print(f'Actual date : {today}')
                print(f'Due date : {product.due_date}')

                if today>product.due_date:
                    product.state = False
                    product.save()



