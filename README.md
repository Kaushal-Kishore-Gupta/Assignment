
# Docs for accessing Backend APIs

## Run Locally

Must have following services pre-installed 
+ python3
+ pip
+ virtualenv

Clone the project

```bash
git clone https://github.com/Kaushal-Kishore-Gupta/Assignment.git
```

Go to the project directory

```bash
  cd Assignment
```

Create Virtualenv

```bash
  virtualenv env
```

Activate Virtualenv

```bash
  source env/bin/activate
```

Install Dependencies
```bash
pip install -r requirements.txt
```
## API Reference

#### Sending Matrix

```http
  POST /api/find_largest/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `matrix` | `list[list]` | **Required**.  |



```json
{
  "matrix":[
[1, 1, 1, 0, 1, -9],
[1, 1, 1, 1, 2, -9],
[1, 1, 1, 1, 2, -9],
[1, 0, 0, 0, 5, -9],
[5, 0, 0, 0, 5]
]
}

```
The result from successful post request will be 
```http
HTTP/1.1 `200 OK`
Content-Type: application/json

{
    "area": 8,
    "number": 1
}
```
## More Examples
```json
{
  "matrix": [
[1, 1],
[1, 1, 1, 1, 2, -9],
[2, -9],
[1, 0, 0, 0, 5, -9],
[5, 0, 0, 0, 5],
[5, 0, 0, 0, 5],
[5, 0, 0, 0, 5],
[5, 0, 0, 0, 5],
[5, 0, 0, 0, 5],
[5, 0, 0, 0, 5],
[5, 0, 0, 0, 5]
]
}

```
The result from successful post request will be 
```http
HTTP/1.1 `200 OK`
Content-Type: application/json

{
    "area": 24,
    "number": 0
}
```



#### Accessing Database

```http
   /admin
```

