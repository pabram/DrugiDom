# DrugiDom

[![Build Status](https://travis-ci.org/pabram/DrugiDom.svg?branch=master)](https://travis-ci.org/pabram/DrugiDom)

### How to set up

To start project:

:::java
./install_requirements.sh && python manage.py migrate
python manage.py runserver

After each `git pull` should apply new migrations

:::java
python manage.py migrate

### HTTP statuses

* 200 - operation succesful (Appear with GET, PUT)
* 201 - operation succesful object created (Appear with POST)
* 204 - operation succesful - no content (Appear with DELETE)
* 400 - incorect/insufficient parameters
* 403 - authentication error or action was forbiden
* 404 - object not found 
* 500 - exception

### API

#### POST /api/documents

Save new user document, need account with permissions.

**Parameters**

* name
* content
* case_status
* staffMember / todo
* resident /todo
* documentType /todo

**Output**

```
    {
        "id": 7,
        "name": "Sample1",
        "content": "Sample2",
        "case_status": "1"
    }
```

#### GET /api/documents

Get user documents

**Parameters**

    none

**Output**

```
[
    {
        "id": 7,
        "name": "Sample1",
        "content": "Sample2",
        "case_status": "1"
    },
    {
        "id": 4,
        "name": "doc",
        "content": "1",
        "case_status": "1"
    }
]
```

#### PUT /api/documents/{id}/

Edit document, need account with permissions. 

**Parameters**

* id 

**Output**

```
{
        "id": 7,
        "name": "Sample1",
        "content": "Sample2",
        "case_status": "1"
}
```

#### DELETE /api/documents/{id}/

Delete document, need account with permissions. 

**Parameters**

* id 

**Output**

* Success
Status 204

* Error

```
{
    "detail": "Not found."
}
```