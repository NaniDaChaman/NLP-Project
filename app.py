from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
from flask import render_template
from flask import url_for
import speechrecon
import os


app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"{secure_filename(file.filename)}")
        #cv2.imshow("og image",cv2.imread(secure_filename(file.filename)))
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        subdclip=speechrecon.main(secure_filename(file.filename))
        print(subdclip)
        return render_template('upl.html',method=False,link=subdclip)

    if request.method=="GET":
        print('This is the url : ',url_for('upload_file'))
        return render_template('upl.html',method=True,act=url_for('upload_file'))

@app.route('/test/<dyn>')
def resp(dyn):
    return f'<h1>{dyn}</h1>'

@app.route('/chillin')
def cool():
    return resp("i am cool")

if __name__ == '__main__':  
   app.run(debug = True)  