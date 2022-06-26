from xml.dom import ValidationErr
from rest_framework.views import APIView
from .serializers import UrlSerializer
from rest_framework import status
from rest_framework.response import Response
from .shortener import generate_short_id
from .models import URL
from .base_env import Baseenv
from rest_framework import generics
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle



class CreateShortUrlView(APIView):

    throttle_classes = [UserRateThrottle]
    """Bu view /createurl/ endpointine gelen isteğini karşılar
    Post methodu içerisinde bodyden gelen datayı serializerdan 
    geçirip validated_datayı alıyoruz. Hataya karşı try except 
    bloğu içerisinde bu işlemleri yapıyoruz
    
    generate_short_id() yi çağırıp longUrl için bir unique id
    elde ediyoruz. Sonrasında daha önce kaydedilmemiş ise db'ye
    kaydediyoruz."""

    serializer = UrlSerializer

    def post(self,request,*args, **kwargs):

        serializer = self.serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)

            short_path= generate_short_id(len(serializer.validated_data['longUrl']))
            short_url = '{}{}'.format(Baseenv.root_url,short_path)

            if not URL.objects.filter(Short_Url=short_url).exists():
                URL.objects.create(Origin_Url=serializer.validated_data['longUrl'],
                Short_Url=short_url,Short_Path=short_path)

            data = {
                "Origin_Url":serializer.validated_data['longUrl'],
                "Short_Url":short_url
            }
            return Response(status=status.HTTP_201_CREATED,data=data)

        except ValidationErr as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=e)


class ListUrlsView(generics.ListAPIView):

    """ Bu view tüm URL objelerini listeler.
    Burada ListAPIView kullanılabilirdi
    fakat serializer kullanmadan da datayı 
    dışarı açmayı göstermek istedim. Ama 
    bu tür durumlarda ListAPIView'ı kullanmak
    hem daha efektif hem de daha sağlıklıdır. """
    throttle_classes = [AnonRateThrottle]
    def get(self,request,*args, **kwargs):

        from django.http import JsonResponse

        try:
            urls = URL.objects.values()
            return JsonResponse(list(urls), safe=False)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
            data="Something is wrong!") 


def redirect(request,shortpath):

    """Class Based Viewlar kullanmadan
    bir func ile view yazmak için kullandım.
    Gelen requestin methoduna göre işlem yapıp 
    Short_Url in Origin_Url ine redirect yapıyoruz.

    param olarak gelen shortpath'i URL tablosunda
    filter edip eğer oluşmuş ise Origin url'ine
    redirect işlemi gerçekleştiriliyor.    

    F() fonksiyonunun kullanımı da gösterilmiştir."""


    from django.shortcuts import redirect
    from django.db.models import F

    if request.method =="GET":

        path = URL.objects.filter(Short_Path=shortpath)
        if path.exists():
            path.update(visit_Count=F('visit_Count')+1)
            return redirect(str(path.first().Origin_Url))



            
        
        

    