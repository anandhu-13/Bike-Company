from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout

from Store.decorators import signin_required
from Store.models import Bike,Service,Order,Category
from Store.forms import RegistrationForm,LoginForm
from django.views.decorators.csrf import csrf_exempt
import razorpay



KEY_ID="rzp_test_tGyW98HIsAU7s4"
KEY_SECRET="eqFjK1cogbMNolEnX0dOZiqQ"







class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm
        return render(request,"register.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        return render(request,"login.html",{"form":form})
    




# localhost:8000/
# method: get,post
# form_class: LoginForm
        
class SigninView(View):

    def get(self,request,*args,**kwargs):
        form=LoginForm
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("index")
        messages.error(request,"invalid credentials")    
        return render(request,"login.html",{"form":form})
    


@method_decorator([signin_required,never_cache],name="dispatch")
class IndexView(View):

    def get(self,request,*args,**kwargs):
        qs=Bike.objects.all()
        return render(request,"index.html",{"data":qs})
    



@method_decorator([signin_required,never_cache],name="dispatch")
class ProductListView(View):

    def get(self,request,*args,**kwargs):
        qs=Bike.objects.all()
        return render(request,"product_list.html",{"data":qs})


@method_decorator([signin_required,never_cache],name="dispatch")
class HomeView(TemplateView):
    template_name="base.html"


@method_decorator([signin_required,never_cache],name="dispatch")
class ContactView(TemplateView):
    template_name="contact.html"




@method_decorator([signin_required,never_cache],name="dispatch")
class SignOutView(View):

   def get(self,request,*args,**kwargs):
      logout(request)
      return redirect("signin")
   

@method_decorator([signin_required,never_cache],name="dispatch")
class WhyUsView(View):
   def get(self,request,*args,**kwargs):
       return render(request,"blog.html")
   



@method_decorator([signin_required,never_cache],name="dispatch")
class BikeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Bike.objects.get(id=id)
        return render(request,"bike_detail.html",{"data":qs})






@method_decorator([signin_required,never_cache],name="dispatch")
class CheckOutView(View):
   
   
    def get(self,request,*args,**kwargs):
      id=kwargs.get("pk")
      qs=Bike.objects.get(id=id)
      return render(request,"checkout.html" ,{"data":qs})
    
    def post(self,request,*args,**kwargs):
      
      email=request.POST.get("email")
      phone=request.POST.get("phone")
      address=request.POST.get("address")
      payment_method=request.POST.get("payment")
      id=kwargs.get("pk")
      Bike_object_obj=Bike.objects.get(id=id)
      total=Bike_object_obj.price
      
      order_create=Order.objects.create(
         user_object=request.user,
         delivery_address=address,
         phone=phone,
         email=email,
         Bike_object=Bike_object_obj,
         total=total,
         payment=payment_method
          )
      
        
      
      Bike_object_obj.is_placed=True
      Bike_object_obj.save()


      if payment_method=="online" and order_create:
          
          client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
          data = { "amount":total*100, "currency": "INR", "receipt": "order_rcptid_11" }
          payment = client.order.create(data=data)

          order_create.order_id=payment.get("id")
          order_create.save()
          
          print("payment initiate",payment)
          context={
             "key":KEY_ID,
             "order_id":payment.get("id"),
             "amount":payment.get("amount")
          }
          return render(request,"payment.html",{"context":context})
        

        
      return redirect("success")
      



@method_decorator(csrf_exempt,name="dispatch")
class PaymentVerificationView(View):  
   def post(self,request,*args,**kwargs):
      client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
      data=request.POST
     
      try:
         client.utility.verify_payment_signature(data)
         print(data)
         order_obj=Order.objects.get(order_id=data.get("razorpay_order_id"))
         order_obj.is_paid=True
         order_obj.save()
         print("******Transaction completed*****")
        

      except:
         print("!!!!!!!Transaction Failed!!!!!!!")
      
      return render(request,"success2.html")








@method_decorator([signin_required,never_cache],name="dispatch")
class OrderSummaryView(View):

    def get(self,request,*args,**kwargs):
         qs=Order.objects.filter(user_object=request.user).exclude(status="cancelled")
         return render(request,"order_summary.html",{"data":qs})
    

class OrderItemRemoveView(View):
    def get(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       order_objk=Order.objects.get(id=id)
       bike_obj=order_objk.Bike_object
       bike_obj.is_placed=False
       bike_obj.save()
       Order.objects.get(id=id).delete()
       return redirect("summary")



class SucessView(View):
   def get(self,request,*args,**kwargs):
       return render(request,"success.html")
