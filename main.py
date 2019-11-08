from flask import Flask, render_template,request,make_response

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    user_name = request.cookies.get("user_name")
    return render_template("index.html",user_name=user_name)

@app.route('/',methods=["POST"])
def index_post():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    response = make_response(render_template("success.html"))
    response.set_cookie("user_name",contact_name)


    return render_template("index.html")


if __name__== "__main__":
    app.run(debug=True,port=5500)



