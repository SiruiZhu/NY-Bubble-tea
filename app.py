from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stores.db'
db = SQLAlchemy(app)


class Store(db.Model):
  __tablename__ = 'stores'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.Integer, primary_key=True)


@app.route("/")
def hello():
    stores = Store.query.all()
    return render_template("list.html", stores=stores)

@app.route("/stores/")
def stores():
  stores = Store.query.all()
  return render_template("list.html", stores=stores)

@app.route("/stores/<index>/")
def store(index):
  store = Store.query.filter_by(index=index).first()
  return render_template("show.html", store=store)

# @app.route("/search")
# def search():
#   name = request.args.get('query')
#   stores = Store.query.filter(Store.store.contains(name)).all()
#   return render_template("search.html", stores=stores)





if __name__ == '__main__':
  app.run(debug=True)