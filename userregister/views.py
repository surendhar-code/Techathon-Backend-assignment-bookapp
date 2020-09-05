from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import book

# Create your views here.

def booklist(request):
    context = {'book_list':book.objects.all()}
    return render(request,"user_register/book_list.html",context)




def bookform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=BookForm()
        else:
            Book=book.objects.get(pk=id)
            form=BookForm(instance=Book)
        return render(request,"user_register/book_form.html",{'form':form})
    else:
         if id == 0:
            form = BookForm(request.POST)
         else:
            Book = book.objects.get(pk=id)
            form = BookForm(request.POST,instance= Book)
         if form.is_valid():
            form.save()
        
         return HttpResponse('updated successfully')





def bookdelete(request,id):
    Book=book.objects.get(pk=id)
    Book.delete()
    return redirect('list/')