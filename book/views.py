from django.shortcuts import render,redirect

from django.views.generic import View
from book.models import Books
from book.forms import Bookform,RegisterationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

class BooksListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        return render(request,"book_list.html",{"data":qs})
    

class BooksDetailsView(View):

    def get(self,request,*ags,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})

class BooksDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        messages.success(request,"book details deleted successfully...!!!")
        return redirect("books-all")
    

class BookCreateView(View):

    def get(self,request,*args,**kwargs):
        form=Bookform()
        return render(request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"new book details is added successfully....")
            return redirect("books-all")
        else:
            messages.error(request,"error..,can't create book data...")
            return render(request,"book_add.html",{"form":form})



class BookUpdateView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=Bookform(instance=obj)
        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=Bookform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,"book details is updated successfully....")
            return redirect("books-all")
        else:
            messages.error(request,"can't update book details....")
            return render(request,"book_edit.html",{"form":form})
         

class RegisterView(View):

    def get(self,request,*args,**kwargs):
        form=RegisterationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"register.html",{"form":form})


class SigninView(View):

    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(uname="username",pwd="password")
            print(user_object)
            if user_object:
                login(request,user_object)
                return redirect("books-all")
        else:
            return render(request,"login.html",{"form":form})

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")   
    

    
