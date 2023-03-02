import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from polls import models, forms


def get_username(request):
    users = []

    username = request.user
    usern = models.Users.objects.get(user=username)

    users.append(username)
    users.append(usern)

    return users
# def get_data(**kwargs):
#     data = []
#     if 'prod_id' in kwargs:
#         product = models.ProductData.objects.get(product_id=kwargs['prod_id'])
#         print(kwargs['prod_id'])
#         data.append(product)

#     if 'id' in kwargs:
#         # store = models.StoreData.objects.get(user=kwargs['usern'])
#         store= models.StoreSales.objects.filter(id=kwargs['id']).values()
#         data.append(store)
#     return data

def delete_store(request, storeid):
    store_name = models.StoreData.objects.get(storeid=storeid)
    store_name.delete()
    return HttpResponseRedirect(reverse('user'))

def update_store(request, storeid):
    usern = get_username(request)
    if request.method == "POST":
        store_model = models.StoreData.objects.get(storeid=storeid)

        st_name = request.POST.get('store_name')
        st_id = request.POST.get('storeid')
        stloc = request.POST.get('storelocation')

        store_model.store_name = st_name
        store_model.storeid = st_id
        store_model.store_location = stloc

        store_model.save()

        return HttpResponseRedirect(reverse('user'))
    else:
        store = models.StoreData.objects.get(store_id=storeid)  
        context = {
                'store': store,
                'usern':usern[1]
            }
        return render(request, 'polls/user/update-store.html', context)




def delete_product(request, productid):
    member = models.ProductData.objects.get(productid=productid)
    print(member)
    member.delete()
    return HttpResponseRedirect(reverse('user'))

def update_product(request, productid):
    usern = get_username(request)
    if request.method == "POST":
        product_model = models.ProductData.objects.get(productid=productid)

        pr_name = request.POST.get('product_name')
        prid = request.POST.get('productid')
        pr_uni = request.POST.get('unit')

        product_model.product_name = pr_name
        product_model.productid = prid
        product_model.unit_price = pr_uni

        product_model.save()

        return HttpResponseRedirect(reverse('user'))

    product = models.ProductData.objects.get(productid=productid)  
    context = {
            'product': product,
            'usern':usern[1]
        }
    return render(request, 'polls/user/update-product.html', context)


@login_required(login_url='login')
def ViewUsers(request):

    usern = get_username(request)
 
    email = getattr(usern[1], 'email')

    products = models.ProductData.objects.filter(user=usern[1])
    stores = models.StoreData.objects.filter(user=usern[1])

    context = {
        'usern': usern[1],
        'email': email,
        'products': products,
        'stores' : stores
    }

    
    return render(request, 'polls/user/detail.html', context)

@login_required(login_url='login')
def add_product(request):

    usern = get_username(request)

    if request.method == "POST":

        product_form = forms.ProductDataForm(request.POST, username = usern[0])

        if product_form.is_valid():

            post = product_form.save(commit = False)
            post.save()
            return redirect('add_product')
    else:
        product_form = forms.ProductDataForm(request.POST, username = usern[0])

    context = {
            'product_form' : product_form,
            'usern': usern[1]
        }
  
    return render(request, 'polls/forms/add_product.html', context)

@login_required(login_url='login')
def add_store(request):
    
    usern = get_username(request)
    
    if request.method == "POST":

        store_form = forms.StoreDataForm(request.POST, username = usern[0])

        if store_form.is_valid():

            post = store_form.save(commit = False)
            post.save()

            return redirect('add_store')
    else:
        store_form = forms.StoreDataForm(request.POST, username = usern[0])

    context = {
            'store_form' : store_form,
            'usern': usern[1]
        }
  
    return render(request, 'polls/forms/add_store.html', context)



@login_required(login_url='login')
def add_sales(request):

    usern = get_username(request)

    if request.method == "POST":

        store_form = forms.SalesDataForm(request.POST, username = usern[0])

        if store_form.is_valid():
            post = store_form.save(commit = False)
            post.save()

            message = 'Page Submitted'
            
        return redirect('add_sales')
    else:
        store_form = forms.SalesDataForm(request.POST, username = usern[0])

    context = {
            'sales_form' : store_form,
            'usern': usern[1]
        }
  
    return render(request, 'polls/forms/add_sales.html', context)

@login_required(login_url='login')
def view_sales(request):

    usern = get_username(request)

    sales = models.StoreSales.objects.filter(user=usern[1])
    context={
        "sales" : sales,
        'usern': usern[1]
    }
  
    return render(request, 'polls/forms/view_sales.html', context)

def export_sales_csv(request):
    
    usern = get_username(request)
    sales_model = models.StoreSales.objects.filter(user=usern[1])
    filename = f'{usern[0]}-sales'
    return  export_csv(sales_model, ['storeid', 'prodid', 'pub_date', 'units_sold'], filename)

def export_store_csv(request):
    
    usern = get_username(request)

    # users = models.Users.objects.get(user=usern[0])
    store_model = models.StoreData.objects.filter(user=usern[1])
    filename = f'{usern[0]}-store'
    return  export_csv(store_model, ['storeid', 'store_name', 'store_location'], filename)

def export_product_csv(request):
    
    usern = get_username(request)
    store_model = models.ProductData.objects.filter(user=usern[1])
    filename = f'{usern[0]}-product'
    return  export_csv(store_model, ['productid', 'product_name', 'unit_price'], filename)


def export_csv(model, list, filename):

    response = HttpResponse()
    
    response['Content-Disposition'] = f'attachment; filename={filename}.csv'

    writer = csv.writer(response)
    writer.writerow(list)

    to_csv = model.values_list(*list)
    for data in to_csv:
        writer.writerow(data)
    return response

def loginPage(request):

    if request.method == "POST":

        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        admin = authenticate(request, username="admin", password=password)

        if admin is not None:
            login(request, admin)
            return redirect('admin')
        elif user is not None:
            login(request, user)
            return redirect('user')
        else:
            messages.success(request, 'Username or Password is incorrect.')   

    context = {}        
    return render(request, 'polls/login.html', context)

def logoutUser(request):
    
    logout(request)
    return redirect('login')