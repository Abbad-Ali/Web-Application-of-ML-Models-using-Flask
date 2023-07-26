from flask import Flask, render_template, request
import pickle 
app = Flask(__name__)
model = pickle.load(open('expense_model.pkl','rb')) #read mode
@app.route("/")
def home():
    return render_template('predictor.html')
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        #access the data from form
        ## Age
        age = int(request.form["age"])
        bmi = int(request.form["bmi"])
        children = int(request.form["children"])
        Sex = int(request.form["Sex"])
        Smoker = int(request.form["Smoker"])
        Region = int(request.form["Region"])
        #get prediction
        input_cols = [[age, bmi, children, Sex, Smoker, Region]]
        prediction = model.predict(input_cols)
        output = round(prediction[0], 2)
        if output > 5000:
            return render_template("predictor.html", prediction_text='Your predicted annual Healthcare Expense is $ {} but it is bad prediction'.format(output))
        else:
            return render_template("predictor.html", prediction_text='Your predicted annual Healthcare Expense is $ {} and it is good prediction'.format(output))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)