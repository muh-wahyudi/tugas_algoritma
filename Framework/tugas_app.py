from flask import Flask, render_template

app = Flask(__name__)

# mengarahkan page beranda
@app.route("/beranda/")
def beranda():
    return "selamat datang di websit saya"

# mengarhkan ke page saya(about tanpa css)
@app.route("/beranda/about_me/saya/")
def saya():
    return render_template('about_1.html')
# mengarhakan ke page about yang menggunakan css
@app.route("/beranda/about_me/")
def about_me():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)