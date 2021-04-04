from main.utils.database import db
from datetime import datetime

class File(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    date_added=db.Column(db.DateTime(),default=datetime.utcnow)
    pneu_pred_score=db.Column(db.Text(),nullable=False)
    pneu_pred_class=db.Column(db.Text(),nullable=False)
    covid_pred_score=db.Column(db.Text(),nullable=False)
    covid_pred_class=db.Column(db.Text(),nullable=False)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"\n >>> {self.name}"


