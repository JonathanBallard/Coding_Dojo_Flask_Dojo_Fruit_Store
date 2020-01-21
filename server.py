from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    # blackberry = request.form['blackberry']
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    student_id = request.form['student_id']
    totalOrder = int(raspberry) + int(apple) + int(strawberry)
    print('charging ' + firstName + ' ' + lastName + ' for ' + str(totalOrder) + ' fruits')
    return render_template("checkout.html", strawTemp = strawberry, raspTemp = raspberry, appleTemp = apple, totalTemp = totalOrder, firstTemp = firstName, lastTemp = lastName, studentTemp = student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    