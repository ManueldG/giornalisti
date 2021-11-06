from django.shortcuts import render
from django.http import HttpResponse

header="""
<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="http://casaalmada.hostinggratis.it/doc/css/reset.css">
        <link rel="stylesheet" href="css/style.css">
        <script src="js/script.js"></script>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Giornalisti</title>
    </head>

     """

body_home = """
<body>

<h1>Titolo!!!</h1>

<a href="contacts/">contatti</a>

</body>
"""

body_contacts = """
<body>

<h1>contacts</h1>
<ul>
    <li>
        Manuel
    </li>
    <li>
        della Gala
    </li>
    <li>
        347143142
    </li>
    <li>
        mdg@sdfsa.com
    </li>
<ul>


</body>

"""

footer = """
    <footer>
    made with &#10084; by MdG
    </footer>
</html>

     """

def home(request):
    html = header+body_home+footer
    return HttpResponse(html)

def contacts(request):
    html = header+body_contacts+footer
    return HttpResponse(html)


