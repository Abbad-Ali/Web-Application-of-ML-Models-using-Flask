from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('print_table.html')
@app.route("/table", methods=['GET','POST'])
def table():
    if request.method == 'POST':
        #access the data from form
        ## Age
        table = int(request.form["table"])
        iteration = int(request.form['upto'])
        table_data=[]
        for i in range(1, iteration+1):
            table_data.append(str(table) +" x " + str(i) + " = " + str(table*i))
        return render_template("print_table.html", prediction_text=table_data)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)