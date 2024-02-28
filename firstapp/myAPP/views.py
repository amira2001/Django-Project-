import datetime
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse 
from http.client import HTTPException 
import json 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from myAPP.models import *
from myAPP.serializers import BookSerializer
# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

@csrf_exempt 
def ADD_LIVRE(request):
    #livre = Book(title="book1",author="Amira")
    #livre.save()
    #context={" auteur :"+ livre.author," titre :"+livre.title}
    if request.method == 'POST':
        data = JSONParser().parse(request)
        titre = data.get('title')
        author = data.get('author')
        if Book.objects.filter(title=titre,author=author).exists() : 
            return HTTPException
        else: 
            book_serializer = BookSerializer(data=data)  
            if book_serializer.is_valid():
                book_serializer.save()
            else:
                return HTTPException
            return JsonResponse(book_serializer.data)
    
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializers = BookSerializer(books,many=True)
        
        return JsonResponse(books_serializers.data,safe=False)

@csrf_exempt 
def LIVRE_CRUD(request,id):
    if request.method == 'DELETE':
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponse("livre supprimer")
    
    if request.method == 'GET':
        book = Book.objects.get(id=id)
        book_serializers = BookSerializer(book)     
        return JsonResponse(book_serializers.data)



@csrf_exempt 
def EMPREINT(request,id_livre,id_user):
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        #id_livre = data.get('id')
        #id_user = data.get('User')
        book = Book.objects.get(id=id_livre)
        book.user = User.objects.get(id=id_user)
        book.emprunte = "True"
        book.date_emprunt = datetime.date.today()
        book.save()
        book_serializers = BookSerializer(book)     
        return JsonResponse(book_serializers.data)


    

