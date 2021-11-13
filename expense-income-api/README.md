
## SOKO BACK END API
## Setup Requirements

    - Git
    - Python 3.8
    - Django 3.2
    - Django REST framework 3.12
    - PostgreSQL
    - Postman
    - Cloudinary
         - CLOUD_NAME
         - API_KEY
         - API_SECRET

    - Heroku cli (if you want to deploy to Heroku)

## Setup Installation

    - Clone the repository
    - Run the following commands in the terminal:
        - cd <path_to_project> (if you cloned the repository)
        - virtualenv env
        - source env/bin/activate
        - pip install -r requirements.txt
        - cp .env.example .env
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py runserver
    - Open Postman to test the API endpoints or use the following link:
        - http://localhost:8000/api/<the_endpoint>

# Rest api 
`GET /api/profiles/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/profiles/

### Response

        HTTP/1.1 200 OK
        Date: Thu, 26 Oct 2021 12:36:30 GMT
        Status: 200 OK
        Connection: close
        Content-Type: application/json
        Content-Length: 74

        [
            {
                "user": 1,
                "bio": "",
                "profile_pic": "image/upload/picha link",
                "contact": "",
                "location": "",
                "notes": [],
                "created_at": "2021-10-26T15:44:22.778462+03:00",
                "updated_at": "2021-10-26T15:44:22.778481+03:00"
            }
        ]

## Get a specific Profile

`GET /api/profiles/id/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/profiles/1/

### Response

        HTTP/1.1 200 OK
        Date: Thu, 26 Oct 2021 12:36:30 GMT
        Status: 200 OK
        Connection: close
        Content-Type: application/json
        Content-Length: 74

        [
            {
                "user": 1,
                "bio": "",
                "profile_pic": "image/upload/picha link",
                "contact": "",
                "location": "",
                "notes": [],
                "created_at": "2021-10-26T15:44:22.778462+03:00",
                "updated_at": "2021-10-26T15:44:22.778481+03:00"
            }
        ]

## Update a Profile

`PUT /api/profiles/id/`

    curl -i -H 'Accept: application/json' -d 'user=1&bio=&profile_pic=&contact=&location=' http://127.0.0.1:8000/api/profiles/1/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 26 Oct 2021 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 74

    [
        {
            "user": 1,
            "bio": "",
            "profile_pic": "image/upload/house.png",
            "contact": "",
            "location": "",
            "notes": [],
            "created_at": "2021-10-26T15:44:22.778462+03:00",
            "updated_at": "2021-10-26T15:44:22.778481+03:00"
        }
    ]

## User List

### Request

`GET /api/users/`

        curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/users/

### Response

        HTTP/1.1 200 OK
        Date: Thu, 26 Oct 2021 12:36:30 GMT
        Status: 200 OK
        Connection: close
        Content-Type: application/json
        Content-Length: 74

        [
            {
                "id": 1,
                "username": "admin",
                "first_name": "",
                "last_name": "",
                "email": "
            }
        ]

## Create New User

`POST api/users/create/`

    curl -i -H 'Accept: application/json' -d '  http://127.0.0.1:8000/api/users/create/

### Response

        HTTP/1.1 201 Created
        Date: Thu, 26 Oct 2021 12:36:30 GMT
        Status: 201 Created
        Connection: close
        Content-Type: application/json
        Content-Length: 74

        [
            {
                "id": 1,
                "username": "admin",
                "first_name": "",
                "last_name": "",
                "email": "
            }
        ]

## User Login

`POST api/auth/login/`

    curl -i -H 'Accept: application/json' -d 'username=admin&password=admin' http://127.0.0.1:8000/api/auth/login/

### Response

            HTTP/1.1 200 OK
            Date: Thu, 26 Oct 2021 12:36:30 GMT
            Status: 200 OK
            Connection: close
            Content-Type: application/json
            Content-Length: 74

            [
                {
                    "id": 1,
                    "username": "admin",
                    "first_name": "",
                    "last_name": "",
                    "email": "
                }
            ]

## Logout User

`POST api/auth/logout/`

    curl -i -H 'Accept: application/json' -d 'username=admin&password=admin' http://127.0.0.1:8000/api/auth/logout/

### Response

            HTTP/1.1 200 OK
            Date: Thu, 26 Oct 2021 12:36:30 GMT
            Status: 200 OK
            Connection: close
            Content-Type: application/json
            Content-Length: 74

## Known Bugs

So far so good there are no bugs related to this project 😎

## Support and contact details 🙂

Reach out to me via email edwinkimathi226@gmail.com

## License

Copyright (c) 2021 Edwin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files , to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
