<div align="center"><img src="https://raw.githubusercontent.com/pallets/flask/refs/heads/stable/docs/_static/flask-name.svg" alt="" height="150"></div>

# Flask

Flask is a lightweight [WSGI] web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around [Werkzeug]
and [Jinja], and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/

## A Simple Example

```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Donate

The Pallets organization develops and supports Flask and the libraries
it uses. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, [please
donate today].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/

# WSGI GET 


<p>WSGI GET adalah metode cara metode get bekerja dalam syntax flask bukan post melainkan get</p>

<p>Cara Kerja WSGI didalam form get html</p>



## Code 


```bash 
# from cgi import parse_qs (telah dihapus oleh python)
# diganti menggunakan from urllib.parse import parse_qs 

Bagian ini adalah mengimport library wsgiref dan menggunakan urllib.parse sebagai parse_qs 
cgi telah dihapus 

from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


# form yang mengikuti namadepan '' dan namabelakang di ikuti variabel di kode python yang tes.get('')
index_form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Tampilan awal Wsgi Form</title>
        <style>
        <!-- style css -->
        </style>
    </head>
    <body>
        <form method="get">
        Nama Depan<br>
        <input type="text" name="namadepan" placeholder="masukan nama depan"><br>
        Nama Belakang<br>
        <input type="text" name="namabelakang" placeholder="masukan nama belakang">
        <input type="submit" value="kirim">
        </form>
    </body>
</html>
"""

# '%s %s' yang berfungsi mengeluarkan hasil dari kode function 
index_page = """
<!DOCTYPE html>
<html>
    <head>
        <title>GET Result</title>
        <style>
        <!-- style css disni-->
        </style>
    </head>
    <body>
    <h1>WSGI GET HASIL</h1>
    <p> HALO, %s %s</p>
    </body>
</html>

"""

# logic menggunakan environ dan QUERY_STRING lalau membuat variabel bernama tes lalu memanggil parse_qs(environ['QUERY_STRING'])
# dan membuat variabel namadepan dan namabelakang untuk menampung data dari form dengan [''])[0] berfungsi untuk tidak
# membuat output list 
# dan memnampung index_page % (namadepan,namabelakang) sebagai variabel body untuk dikirim ke hasil di index_page 
def application(environ,start_response):
    if (environ['QUERY_STRING']):
        tes = parse_qs(environ['QUERY_STRING'])
        namadepan = tes.get('namadepan',[''])[0]
        namabelakang = tes.get('namabelakang',[''])[0]
        body = index_page % (namadepan,namabelakang)

    else:
        body = index_form 

    # status 
    status = '200 OK'
    
    # text type for html and length for body 
    headers = [
    ('Content-type','text/html'),
    ('Content-length',str(len(body)))
    ]
    start_response(status,headers)
    return [body.encode('utf-8')]

# menjalankan server di localhost port 5000
if __name__=="__main__":
    server = make_server('localhost',5000,application)
    server.serve_forever()
        


```




