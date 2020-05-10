from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/protect')
def protect():
    return render_template('protect.html')

@app.route('/rc')
def rc():
    return render_template('rc.html')

@app.route('/stayhome')
def stayhome():
    return render_template('stayhome.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/article2')
def article2():
    return  render_template('article2.html')

@app.route('/article3')
def article3():
    return render_template('article3.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/hangman')
def hangman():
    return render_template('hangman.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/gamemovie')
def gamemovie():
    return render_template('gamemovie.html')

@app.route('/bakecook')
def bakecook():
    return render_template('bakecook.html')

@app.route('/contactus')
def contactus():
    return render_template('contact_us.html')



if __name__ == '__main__':
    app.run()
