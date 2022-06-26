from importlib.resources import path
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import URL
from .base_env import Baseenv
import json

class UrlApiTestCase(APITestCase):

    def test_create_url(self):
        """
        Bir url için endpointe post istek atıp
        dönüş değerlerini test ediyoruz. 
        """
        url = reverse('Create-Url')
        data = {"longUrl":"https://www.deliveryhero.com/"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(URL.objects.count(), 1)
        self.assertEqual(URL.objects.get().Origin_Url,data.get("longUrl"))

    def test_list_urls(self):

        origin_url ="http://www.x.com"
        short_url = str(Baseenv.root_url+"Test")
        short_path ="Test"

        URL.objects.create(Origin_Url=origin_url,
            Short_Url=short_url,Short_Path=short_path)

        url = reverse("List-Url")
        response = self.client.get(url,format='json')
        json_response = json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response[0]["Origin_Url"],origin_url)
        self.assertEqual(json_response[0]["Short_Url"],short_url)
        self.assertEqual(json_response[0]["Short_Path"],short_path)
