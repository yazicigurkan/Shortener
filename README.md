# Django - Shortener REST API


Bu proje bir Django projesi olarak url kısaltma işlemi üzerine kurulmuş bir API tasarımı içermektedir.

## Özellikler
- Kısa URL oluşturma
- URL'leri listeme
- Kısa URL den gerçek URL'e yönlendirme


Proje içerisindeki endpointler sayesinde istediğiniz bir url'i kısaltabilirsiniz. Bunun yanında kısalttığınız url'i kullanarak gerçek url'e yönlenme yapabilirsiniz. Oluşturduğunuz kısa url'leri listeleyebilir ve bu kısa url üzerinden kaç kere yönlenme gerçekleşmiş görebilirsiniz.

## Kullanılan Teknolojiler

Proje kapsamında kullanılan Teknolojiler aşağıdaki gibidir:

- [Django] -  Python-based web framework
- [Django REST framework ] - Web APIler geliştirmek için güçlü ve esnek bir framework
- [Postgresql] - Open-source ilişkisel veritabanı yönetim sistemi
- [Docker] - Open-source konteynır teknolojisi


## Kurulum

Projeyi lokalinize indirdikten sonra sırası ile aşağıdaki adımları izleyebilirsiniz.

 Uyarı : Bilgisayarınızda `Docker` kurulu olmalıdır . Kurulu değil ise [Docker] linkinden kurulumunuzu gerçekleştirebilirsiniz.
 
Terminal ile Proje dizinine gelerek aşağıdaki adımları izliyoruz.


Docker Compose ile dizinde yer alan docker-compose.yml dosyasını ayağa kaldırıyoruz:

```sh
docker-compose up
```

Swager dökümantasyonu gözükmesi için...

```sh
docker exec -it shortener_web_1 bash
```
 Superuser Oluşturmak için.
 
```sh
python3 manage.py createsuperuser --username Django-shortener --noinput --email "django@example.com"
```

bash'ten çıkış yapmak için.

```sh
exit
```

## Endpointler

Verilen Endpointler vasıtası ile kısa urller oluşturup listeleyebilirsiniz.

| Method | URI | Request Body | 
| ------ | ------ | ------ |
| POST | http://localhost:8000/create-url/ |"longUrl":"https://www.deliveryhero.com/" |
| GET | http://localhost:8000/list-urls/ |


## Redirect (Yönlendirme)

Oluşturmuş olduğunuz kısa URL'inizi kopyalayıp browserın adres bar'ına yapıştırınca kısa URL'üzerinden gerçek URL'e yöneldiriliceksiniz. Daha sonra ``` list-urls ``` endointine GET isteği atın ve kısa URL'iniz üzerinden kaç kere yönlendirme olmuş görün.


Projeyi durmak için:

```sh
docker-compose down
```
yapabilirsiniz.

Aşağıdaki curl örneklerinizi terminalizinde deneyebilirsiniz.

- Create URL :

```sh
curl --location --request POST 'http://127.0.0.1:8000/create-url/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "longUrl":"https://www.deliveryhero.com/"
}'
```
- List URLs :

```sh
curl --location --request GET 'http://127.0.0.1:8000/list-urls/'
```

   [django]: <https://www.djangoproject.com/>
   [Django REST framework]: <https://www.django-rest-framework.org/>
   [Postgresql]: <https://www.postgresql.org/>
   [Docker]: <https://www.docker.com/>

