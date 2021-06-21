# Test API BOOKS

Development by [Andres Vasquez](https://github.com/anfevazu)


## Run project :
```sh
docker-compose up --build
```

## Endpoints :
### Login :
- http://127.0.0.1:8000/api/v1/books/login/
    ### Method POST
    ### body
    ```json
    {
        "username" : "admin",
        "password" : "admin
    }
    ```
    ### Response
    ```json
    {
        "token": "d7738f5bc7cb78a46eebca02d47c42233d4f9773"
    }
    ```
__________
### Register :
- http://127.0.0.1:8000/api/v1/books/register/
    ### Method POST
    ### body
    ```json
    {
        "username": "andy",
        "email": "andresvz07@hotmail.com",
        "password": "Andres123#"
    }
    ```
    ### Response
    ```json
    {
       "username": "andy",
       "email": "andresvz07@hotmail.com",
    }
    ```
-----
### Delete Book :
- http://127.0.0.1:8000/api/v1/books/<book-id>
    ### HEADER
    ```
    Authorization Token 07d4afb94777acba8f1b86e1b56790f896583e98
    ```
    ### Method DELETE
    ### body
    ```json
    {

    }
    ```
    ### Response
    ```json
    {

    }
    ```
-----
### Delete Book :
- http://127.0.0.1:8000/api/v1/books?search="QUERY STRING"
    ### HEADER
    ```
    Authorization Token 07d4afb94777acba8f1b86e1b56790f896583e98
    ```
    ### Method GET
    ### body
    ```json
    N/A
    ```
    ### Response
    ```json
    {
    "total": 193,
    "page": 1,
    "page_size": 15,
    "results": [
        {
            "id": 224,
            "authors": [],
            "categories": [],
            "created": "2021-06-21T11:26:29.087399-05:00",
            "modified": "2021-06-21T11:26:29.087456-05:00",
            "title": "Programacion Lineal y Decisiones Economicas",
            "sub_title": null,
            "publish_date": null,
            "editor": "Universidad Catolica Andres",
            "description": "Planteado de esa forma , el problema de <b>programación</b> lineal se podría enfocar <br>\nasí : existe una serie de actividades alternativas ( n ) , para alcanzar un <br>\ndeterminado objetivo ( maximizar o minimizar Z ) , y se cuenta con una cantidad <br>\nlimitada&nbsp;...",
            "image": "http://books.google.com/books/content?id=cGLZ7W0BzQoC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
            "source_book": "db"
        },
    ......
    ```
-----

### Admin Panel :
- http://127.0.0.1:8000/admin

### credentials
- Default credentials

```json
{
    "username": "admin",
    "password": "admin",
}
```
------
