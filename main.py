# from cgi import parse_qs (telah dihapus oleh python)
# diganti menggunakan from urllib.parse import parse_qs 

from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

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

if __name__=="__main__":
    server = make_server('localhost',5000,application)
    server.serve_forever()
        


