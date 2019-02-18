from flask import Flask, render_template

app = Flask(__name__)

# function binding
@app.route("/")
def home():
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello C4E, haha"

@app.route("/hi/<name>")
def hi_nam(name):
    return "Hi " + name

@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    s = x + y
    return str(s)

@app.route("/posts/<int:index>")
def posts(index):
    titles = [
        "Trời mưa to quá",
        "Trời nắng quá",
        "Trời nhiều mây quá",
        "Trời đẹp quá"
    ]
    contents = [
        "Ở nhà ngủ",
        "Đi tắm biển thôi",
        "Chắc chuẩn bị mưa rồi",
        "Tôi đi chơi cùng bạn bè"
    ]
    t = titles[index]
    c = contents[index]
    return render_template("post.html", title = t, content = c)

@app.route("/movie")
def movie():
    return render_template("movie.html" , name = "Deadpool" , image = "https://www.mezcotoyz.com/mas_assets/cache/image/1/0/4/f/4175.Jpg")

@app.route("/movies")
def movies():
    # movie_titles = [
    #     "Deadpool",
    #     "Black widow",
    #     "Captain America"
    # ]
    movie_list = [
        {
            "title": "Deadpool",
            "image": "https://is1-ssl.mzstatic.com/image/thumb/Video5/v4/50/bd/6e/50bd6e23-ad1a-c1f0-1022-de0280909116/pr_source.lsr/268x0w.png"
        },
        {
            "title": "Black widow",
            "image": "https://cdn.vox-cdn.com/thumbor/tusPQdkdtQ2AqegBDJMAKv9amu4=/0x0:1280x640/1200x800/filters:focal(580x195:784x399)/cdn.vox-cdn.com/uploads/chorus_image/image/60256343/black-widow.0.jpg"
        },
        {
            "title": "Captain America",
            "image": "https://genknews.genkcdn.vn/thumb_w/600/2016/captain-america-the-first-avenger-2011-5973-poster-1462360096815.jpg"
        }
    ]
    return render_template("movies.html", movies = movie_list)
if __name__ == "__main__":
    app.run(debug=True)