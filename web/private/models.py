from web.extensions import db


class SomeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(80), unique=False, nullable=True)

    def __repr__(self):
        return self.value
