from django.shortcuts import render
from .models import  Category,Movie

# kategori_liste= ["macera","romantik","dram","bilim kurgu"]
# film_liste = [
#     {
#         "id":1,
#         "film_adi":"film1",
#         "aciklama":"film1 aciklama",
#         "resim": "1.jpeg",
#         "anasayfa":True
#     },
#      {
#         "id":2,
#         "film_adi":"film2",
#         "aciklama":"film2 aciklama",
#         "resim": "2.jpeg",
#         "anasayfa":True
#     },
#      {
#         "id":3,
#         "film_adi":"film3",
#         "aciklama":"film3 aciklama",
#         "resim":"3.jpeg",
#         "anasayfa":False
#     },
#      {
#         "id":4, 
#         "film_adi":"film4",
#         "aciklama":"film4 aciklama",
#         "resim":"4.jpeg",
#         "anasayfa":False
#     },
# ]

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler":Movie.objects.filter(anasayfa = True)
    }
    return render(request,'index.html',data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler":Movie.objects.all()
    }
    return render(request,'movies.html',data)

def moviedetails(request,id):
    data = {
       "movie":Movie.objects.get(id = id)
    }
    return render(request,'details.html',data)


