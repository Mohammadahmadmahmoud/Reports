from django.shortcuts import render,redirect
from django.http import HttpResponse
#from sqlalchemy.engine import default
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters  import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .decorators import notLoggedUsers , allowedUsers
from  django.contrib import messages

 

# Create your views here.

# function to view the customer details

def main(request):
    return render(request, 'launch/home.html')


# customer details specifiecly  
 
@login_required(login_url = 'Login')
@allowedUsers(allowedGroups=['admin'])
def dashboard(request):
    customere = Customer.objects.all()

    tags = Tag.objects.all()
    announcement = Announcement.objects.all()
    cont = Announcement.objects.all()
    order = Order.objects.all()
    t_order = order.count()
    s_order = order.filter(status='success').count()
    p_order = order.filter(status='pending').count()
    f_order = order.filter(status='failed').count()
    
    context = {
        'announce': announcement,
        'order': order,
        'cons': cont,
        't_order': t_order,
        's_order': s_order,
        'p_order': p_order,
        'f_order': f_order,
        'marketing': customere
    }
    return render(request, 'launch/dashboard.html', context)

 
@login_required(login_url = 'Login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)  # variable looking for specific ID Customer  to show in templates
    serch_filter = OrderFilter()
    order = customer.order_set.all()
    context = {'marketing': customer,
               'order': order,
               'serch_filter':serch_filter
               }
    return render(request, 'launch/customer.html', context)

 
@login_required(login_url = 'Login')
def announcement(request):
    announcements = Announcement.objects.all()
    return render(request, 'launch/announcement.html', {'announce': announcements})
 
@login_required(login_url = 'Login')
def orders(request ):
    order = Order.objects.all( )  # variable storing Customer data to show in templates
    serch_filter = OrderFilter(request.GET , queryset = order)
    order = serch_filter.qs
    context = {
               'order': order,
               'serch_filter':serch_filter
               }
    return render(request, 'launch/orders.html', context)

# def create_order(request):
#     form = Order_Form()
#     if request.method == 'POST':
#         form = Order_Form(request.POST)
#         if form .is_valid():
#             form.save()
#             return redirect('dashboard')
#     context = {'form':form}
#     return render(request,'launch/my_Forms.html', context)

def create_order(request,pk):
    OrderFormSet =  inlineformset_factory(Customer,Order,fields=('announcement','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST' :
        formset = OrderFormSet(request.POST , instance=customer)
        if formset .is_valid():
            formset.save()
            return redirect('orders')
    context = {'formet':formset}
    return render(request,'launch/my_Forms.html', context)


 
 
 
 
@login_required(login_url = 'Login')
def update_announcement(request,pk):
    announcement = Announcement.objects.get(id=pk)
    form = Announce_Form(instance=announcement)
    if request.method == 'POST':
        form = Announce_Form(request.POST,instance=announcement)
        if form .is_valid():
            form.save()
            return redirect('announcement')
    context = {'form':form}
    return render(request, 'launch/create_announcement.html', context)

 
@login_required(login_url = 'Login')
def delete_announcement(request,pk):
    announcement = Announcement.objects.get(id=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('dashboard')
    context = {'announcement':announcement}
    return render(request, 'launch/delete_announcement.html', context)
 
@login_required(login_url = 'Login')
def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = Order_Form(instance=order)
    if request.method == 'POST':
        form = Order_Form(request.POST,instance=order)
        if form .is_valid():
            form.save()
            return redirect('orders')
    context = {'form':form}
    return render(request, 'launch/my_Forms.html', context)
 
@login_required(login_url = 'Login')
def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')
    context = {'order':order}
    return render(request, 'launch/delete_order.html', context)
 
@notLoggedUsers
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUser()
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form .is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request , user + '  ' + 'Created Successfully !')
                return redirect('Login')    
        context = {'form':form}
        return render(request,'launch/register.html',context)
@notLoggedUsers
def Login(request):
         
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')   
            user = authenticate(request , username=username, password=password)
            if  user is not None:
                login(request, user)
                return redirect('dashboard')
            
        context={}
        return render(request,'launch/Login.html',context)

def user_logout(request):
    logout(request)
    return redirect('Login')

 
