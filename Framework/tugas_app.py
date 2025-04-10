from flask import Flask, render_template

app = Flask(__name__)


# mengarahkan page beranda
# @app.route("/")
# def home():
#     return "selamat datang di websit saya, ini adalah halaman home"


# mengarhakan ke page about yang menggunakan css
@app.route("/beranda/about_me/")
def about_me():
    return render_template('about.html')

# mengarahkan ke website yang bisa menambahkan string, integer dll
@app.route("/my_name/<string:nama>")
def getnama(nama):
    return "hallo nama saya adalaha {}".format(nama)

@app.route("/my_name2/<name>")
def user(name):
    return f"Hello, {name}!"

@app.route('/my_name_id/<int:user_id>')  # Hanya menangani variabel selain string
def user_id(user_id):
    return f"User ID: {user_id}"

#ke website dengan menggunakan html
@app.route('/my_name_html/<name>')
def my_name(name):
    return render_template('my_name.html', username=name)

# website dengan variabel global
app_name = "My Flask App" 
@app.route('/')
def home():
    return f"Welcome to {app_name}!"

@app.route('/my_name_data')
def data():
    user = {"name": "wahyudi", "age": 19, "city": "makassar"}
    return render_template('data.html', user=user)


@app.route("/beranda/users/")
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