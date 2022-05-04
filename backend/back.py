from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<tag>')
def success(name):

   return 'Done %s' % tag

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')