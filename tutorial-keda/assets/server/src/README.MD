# Server

## Python 🐍

First we decide to implement our server with the **_Flask_** framework.

- The [**Flask**](https://flask.palletsprojects.com/en/2.2.x/) framework is a lightweight **_Python_** framework

### Our project structure

File structure for the server

```cmd
- /src
    - /templates
        - index.html
    - flaskServer.py
```

Quick links:

- [templates](./templates/)
- [index.html](./templates/index.html)
- [flaskServer.py](./flaskServer.py)

## flaskServer.py 🖥️

In this file we develop our Flask server.

The interesting part in this file is that we used the **flask_cors**.

### CORS ❔

(Cross-Origin Resource Sharing).

Browsers now restrict web pages from making requests to a different domains than the one that served the web page, unless the server explicitly allows it, we can think that this not an error but a security measure to secure users or the website which you are accessing from a potential security breach. To resolve this issue, we can use the Flask-CORS package to enable CORS to our Flask server.
[**CORS**](https://www.contentstack.com/docs/developers/how-to-guides/understanding-and-resolving-cors-error/)

Now to use CORS in our Flask code we just needed to install the CORS package using the following command:

```cmd
pip install Flask-CORS
```

### ServerCode 📑

```python
from flask_cors import CORS
# ...
CORS(app)
```

With this two lines we implement the CORS package in our code.

```python
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_url', methods=['GET'])
def get_url():
    google_url = "https://www.google.com"
    return jsonify({"url": google_url})
```

We define two methods.

- index()
- get_url()

**index()**

So to run our code and overall html with the Flask we need to create the directory templates (_example name_), and then use the **_render_template()_** function. We also add the rout path **'/'**, and when is accessed the Server just renders the **index.html** file in the templates directory.

**get_url()**

Here we just hard code a URL in this case *www.google.com* and just return the URL.

## index.html 🌐

In the **index.html** file we implement a client with a button where the user can click it and send a get request to the server. So to take the **URL** of the server.

We used XMLHttpRequest object to send a GET requests to our Flask server.

```javascript
            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if (this.readyState === 4 && this.status === 200) {
                    const data = JSON.parse(this.responseText);
                    window.location.href = data.url;

```

1. We listens for changes in the request's state, and when the request is completed means:
   - **(readyState === 4) and (status === 200)**
     both should be successful,
2. it parses the JSON response
   - **const data = JSON.parse(this.responseText);**
3. redirects the browser to the received URL
   - **window.location.href = data.url;**.

#### XML HttpRequest

The XMLHttpRequest object can be used to request data from a web server. Like our web server.

Good resource for
[HttpRequest](https://www.w3schools.com/xml/xml_http.asp)

## QR Code

For the **_Qr Code_** I did some changes on the initial version of the code.

- I create a folder with the name **static** under the **src** directory the purpose of this file is to store static files. But I store only the **_qrcode.min.js_** file. I used this because it is required from the QRCode.js library so to create the QRCode.
- I update the **StaticServer.py** to **app.py** so make some new configurations to our Flask server so to make it serve correctly the new **QRCode** implementation. I included the absolute paths for **\*templates** and the **static** directory so to ensure that Flask will locate both of them correctly when we initialize it.

```python
    template_static_directory = os.path.abspath('src/templates')
    static_static_directory = os.path.abspath('src/static')
```

- Last but not leastI developed the **index.html** updating the script reference for the **qrcode.min.js** file and I use the **url_for** function from Flask.

```htlm
<script src="{{ url_for('static', filename='qrcode.min.js') }}"></script>
```

In our html file I implemented a **function** name **_QrCodeGenerator()_** this is our main function where the QR Code generates. We need to pay attention to the `const serverUrl = "http://192.168.0.106:5000"; ` This IP should be our (laptop's / pc's or server's) address. You can find your machine's address first open your **\*cmd**.

- For Windows: `ipconfig`. There just look your IPv4 address from your active adapter.
- For Mac: `ifconfig`. You need to see the **inet** address under your active adapter. I think for MAC is something like: en0 for wired.
- For Linux: `hostname -I`. For linux with this command it's easy this command will just show your local IP address.

Finally, this IP should be changed to our Flask app too

The Qrcode library tha I used is:[QRcode](https://github.com/davidshimjs/qrcodejs)

## Other Resources

1. For Flask I read the documentation of the flask framework: [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
2. As I mentioned before for the HTLM page I used the [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest) and also I found very interesting the [AJAX Introduction](https://www.w3schools.com/xml/ajax_intro.asp) from W3School.
3. Finally, I handle the **_CORS_** (Cross-Origin Resource Sharing) and I used the [CORS](https://flask-cors.readthedocs.io/en/latest/) Flask library. And I read for what is the CORS from the [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
