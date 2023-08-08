from flask import Flask, render_template, request, jsonify
import static.other.scripts.preprocessing as prep

app = Flask(__name__)


@app.route("/")
def main_site():
    return render_template("main.html")


@app.route("/documentation")
def documentation():
    return render_template("documentation.html")


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    user_input = ""
    output_value = ""
    if request.method == "POST":
        user_input = request.form.get('user_input')
        print(f"User inserted: {user_input}")
        output_value = prep.preprocess(user_input)

        return jsonify(output_value=output_value)

    return render_template("calculator.html", output_value=output_value, user_input=user_input)


@app.route("/functions")
def functions():
    return render_template("functions.html")


@app.route("/converter")
def converter():
    return render_template("converter.html")


if __name__ == '__main__':
    #app.run('192.168.1.13', debug=True)
    app.run()
