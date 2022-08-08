from web.extensions import db


class LogbookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80), unique=False, nullable=False)
    last = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'{self.first} {self.last}'
