from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")


@app.route("/hello")  # define a route with a variable in it.
def hello_user():  # function to return html page for user.
    username = request.args.get("x")
    return f"<h1>Hello, {username}!</h1>"  # return a string to html page.


@app.route("/math", methods=["POST"])  # define a route with a variable in it.
def math_operation():
    if request.method == "POST":
        ops = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        if ops == "add":
            result = f"The sum of {num1} and {num2} is: {num1 + num2}"
        elif ops == "subtract":  # subtract a number from another number.
            result = f"The difference of {num1} and {num2} is: {num1 - num2}"
        elif ops == "multiply":  # multiply two numbers together.
            result = f"The product of {num1} and {num2} is: {num1 * num2}"
        elif ops == "divide":  # divide two numbers together.
            result = f"The quotient of {num1} and {num2} is: {num1 / num2}"
        return render_template("results.html", result=result)


@app.route("/postman_data", methods=["POST"])  # define a route with a variable in it.
def math_operation1():
    if request.method == "POST":
        ops = request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])
        if ops == "add":
            result = f"The sum of {num1} and {num2} is: {num1 + num2}"
        elif ops == "subtract":  # subtract a number from another number.
            result = f"The difference of {num1} and {num2} is: {num1 - num2}"
        elif ops == "multiply":  # multiply two numbers together.
            result = f"The product of {num1} and {num2} is: {num1 * num2}"
        elif ops == "divide":  # divide two numbers together.
            result = f"The quotient of {num1} and {num2} is: {num1 / num2}"
        return jsonify({"result": result})


if (
    __name__ == "__main__"
):  # if this module is the main one, then execute the following code.
    app.run(host="0.0.0.0")
