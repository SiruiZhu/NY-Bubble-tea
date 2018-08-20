from flask_frozen import Freezer
from app import app, Store

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def store():
    for store in Store.query.all():
        yield { 'index': store.index }

if __name__ == '__main__':
    freezer.freeze()