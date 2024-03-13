from flask import Flask , render_template , request , jsonify
import prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# api listening to POST requests and predicting sentiments
@app.route('/predict' , methods = ['POST'])
def predict():

    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status' : 'error',
                    'message' : 'Empty Review'}
    
    else:

        # calling the predict method from prediction.py module
        sentiment , path = prediction.predict(review)
        response = {'status' : 'success',
                    'message' : 'Got it',
                    'sentiment' : sentiment,
                    'path' : path}

    return jsonify(response)



# Creating an API to save the review, user clicks on the Save button
@app.route("/save-entry", methods=["POST"])

def save_entry():
    date = request.json.get("date")
    save_text = request.json.get("text")
    emotion = request.json.get("emotion")
    entry = date + "," + save_text + "," + emotion + ","
    file_handler = open('static/assets/data_files/data_entry.csv', 'a')
    file_handler.write(entry +'\n')
    return jsonify("success")

if __name__  ==  "__main__":
    app.run(debug = True)