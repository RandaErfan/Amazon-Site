from django.shortcuts import render ,reverse, redirect



# Create your views here.
things=[
	{"id":1,"product_name":'HP', "img":"l1.jpg"},
	{"id":2,"product_name":'Dell', "img":"l2.jpg"},
	{"id":3,"product_name":'Lenavo', "img":"l3.jpg"}]

def home(request):

	return render(request,'blog/home.html' ,context={'things':things})

def delete(request, thing_id):
    course = product.objects.get(id=thing_id)
    course.delete()
    bact_to_url = reverse('blog-home')
    return redirect(bact_to_url)

def show(request, id):
    thss = filter(lambda thing: thing["id"] == id, things)
    # print(list(stds)[0])
    thing = list(thss)[0]
    return  render(request, 'blog/show.html', context={"thing":thing})
def delete(request):
    thi=things.get_specific_thing(id)
    thi.delete()
    url_to_go=reverse('blog-home')
    return redirect(url_to_go)

def about(request):
    return render(request,'blog/about.html')

def contact(request):
	return render(request,'blog/contact.html')