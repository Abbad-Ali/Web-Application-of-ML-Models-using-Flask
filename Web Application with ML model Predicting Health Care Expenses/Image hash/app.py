from flask import Flask, render_template, request
import hashlib
import os

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('image.html')
@app.route("/image", methods=['GET','POST'])

def image():    
    if request.method == 'Post':
        file = request.files['file']
        im_bytes = os.path.join(file.filename)
        im_bytes.save(im_bytes)
        with open(im_bytes, 'rb') as f:
            im_images= f.read()
            im_hash = str(hashlib.md5(im_images).hexdigest())
    return render_template('image.html', md5_hash=im_hash)
if __name__ == "__main__":
    app.run(debug=True)
