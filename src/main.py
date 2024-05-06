from flask import Flask, request, jsonify;

app = Flask(__name__);

@app.route('/')
def home():
    return '';

############
#  Return  #
############

@app.route('/get-next-line')
def getNextLine():
    return '';

##################
#  Server Start  #
##################

if __name__ == '__main__':
    app.run(debug=True);