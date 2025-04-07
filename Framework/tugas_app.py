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


@app.route("/beranda/user/")
def users():
    user_list = ["denis", "toufik", "raha", "arjun"]
    return render_template('users.html', users=user_list)


@app.route('/beranda/mahasiswa/')
def mahasiswa():
    daftar_mahasiswa = [
        {"nama": "denis", "nilai": 92},
        {"nama": "toufik", "nilai": 80},
        {"nama": "raha", "nilai": 65},
        {"nama": "arjun", "nilai": 55},
    ]
    return render_template('mahasiswa.html', mahasiswa=daftar_mahasiswa)

if __name__=="__main__":
    app.run(debug=True)