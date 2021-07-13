from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/admin/<name>")
def admin(name):
    if name == "Adam":
        return redirect('/admin/{}'.format(name))
    else:
        return redirect('/guestpg/{}'.format(name))


@app.route("/guestpg/<name>")
def guestpg(name):
        return "I am the guest. My name is %s" % name


@app.route('/payment/<int:sal>')
def payment_page(sal):
    if sal >= 20000:
        return "You are rich"
    else:
        return redirect('https://www.sahomeloans.com/%27%27')


if __name__ == 'main':
    app.debug = True
    app.run()