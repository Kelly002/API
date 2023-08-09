from flask import Flask

app = Flask("meu app")

@app.route('/')

def home():
    return "Minha primeira aplicação"
app.run()
