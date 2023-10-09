from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponse
from products.models import product ,Category ,User
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.
def index(request):
	products=product.objects.all()
	return render(request,'products/index.html',{"products":products})

def show(request, product_id):
    prod = product.get_specific_product(id=product_id)
    return  render(request, 'products/show.html',{"product":prod})

def about(request):
    return render(request,'products/about.html')

def contact(request):
	return render(request,'products/contact.html')

def delete(request, product_id):
    prod = product.get_specific_product(product_id)
    prod.delete()
    bact_to_url = reverse('products-index')
    return redirect(bact_to_url)

def create(request):
    categories = Category.get_all_categories()
    if request.method == 'POST':

        if request.POST['name']=='' or request.POST['price']=='' or request.POST['description']=='' :
            return render(request, 'products/create.html', context={"categories":categories})


        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None

            category= None
        if 'category_id' in request.POST:
            category = Category.get_specific_category(request.POST['category_id'])

        prod =product(name=request.POST['name'], current_price=request.POST['price'], image=image, description=request.POST['description'], category=category)
        prod.save()
        url = reverse('products-index')
        return redirect(url)
    return render(request, 'products/create.html', context={"categories":categories})

def createViaForm(request):
    form  = productForm()

    if request.method == 'POST':
 
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                image = request.FILES['image']
            else:
                image = None

            track = None
            if 'track_id' in request.POST:
                category = Category.get_specific_category(request.POST['category_id'])

            prod = product(name=request.POST['name'], email=request.POST['current_price'], image=image,
                              age=request.POST['description'], category=category)
            prod.save()
            url = reverse('products-index')
            return redirect(url)

        print(form.errors)
        return render(request, 'products/createbymodel.html', context={"form":form})


    return render(request, 'products/createbymodel.html', context={"form":form})





def createViaModelForm(request):
    form  = productModelForm()
    if request.method == 'POST':
        form  = productModelForm( request.POST, request.FILES)
        if form.is_valid():

            form.save()
            url = reverse('products-index')
            return redirect(url)

        return render(request, 'products/createbymodel.html', context={"form": form})


    return render(request, 'products/createbymodel.html', context={"form":form})


def edit(request,product_id):
    categories = Category.get_all_categories()
    prod = product.get_specific_product(product_id)
    if request.method == 'POST':

        prod.name = request.POST['name']
        prod.description=request.POST['description']
        prod.current_price = request.POST['price']
        prod.image = request.FILES['image']
        prod.email=request.POST['email']
        category = Category.get_specific_category(request.POST['category_id'])
        prod.category=category
        prod.save()
        url = reverse('products-index')
        return redirect(url)

    return render(request, 'products/update.html', context={'product': prod, 'categories':categories})

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        return redirect('products-index')


    return render(request, 'products/login.html')


def logout(request):
    return render(request,'products/logout.html')



