from flask import Flask, render_template, request
import static.other.scripts.preprocessing as prep

app = Flask(__name__)


@app.route("/")
def main_site():
    return render_template("main.html")


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    user_input = ""
    output_value = ""
    if request.method == "POST":
        user_input = request.form.get('user_input')
        print(f"User inserted: {user_input}")
        output_value = prep.preprocess(user_input)

    return render_template("calculator.html", output_value=output_value, user_input=user_input)


if __name__ == '__main__':
    app.run()
