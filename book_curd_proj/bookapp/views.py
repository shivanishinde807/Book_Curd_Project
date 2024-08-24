from django.shortcuts import render,redirect
from bookapp.models import Book

# Create your views here.
def home(request):
    context = {}
    context['num1']=1000
    context['name']='shivani'
    context['num2']=150
    context['data']=[10,20,30,40]

    return render(request,'index1.html')
def addbook(request):
    return render(request,'addbook.html')

def books(request):
    context = {}
    data = Book.objects.all()
    print(type(data))
    context['books']=data
    return render(request,'allbook.html',context)

def savebook(request):
    #using GET
    #print(request.method) #GET
    # t=request.GET['title']
    # a=request.GET['author']
    # p=int(request.GET['price'])
    #print(title,author,price)

    t = request.POST['title']
    a = request.POST['author']
    p = int(request.POST['price'])

    b = Book.objects.create(title=t,author=a,price=p)
    #print('book added')
    b.save()
    #return render(request,'index1.html')
    return redirect('/list')

def editBook(request,rid):
    book = Book.objects.filter(id=rid)
    print(book)
    context={}
    if request.method == "GET":
        context['book'] = book[0]
        return render(request,'editbook.html',context)
    else:#POST
        t=request.POST['title']
        a=request.POST['author']
        p=int(request.POST['price'])
        book.update(title=t,author=a,price=p)
        return redirect('/list')

def deleteBook(request,rid):
    book = Book.objects.filter(id=rid)
    book.delete()
    context={'success': 'Book deleted!!'}
    return render(request,'allbook.html',context)
    return redirect('/list')


         



    
