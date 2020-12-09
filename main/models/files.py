from main.utils.database import db
from datetime import datetime

class File(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    date_added=db.Column(db.DateTime(),default=datetime.utcnow)
    predictions=db.Column(db.Text())
    score=db.Column(db.Text())
    predicted_class=db.Column(db.String(255),nullable=False)


    # def __init__(self,name,predictions,score,date_added):
    #     self.name=name
    #     self.predictions=predictions
    #     self.score=score
    #     self.date_added=date_added

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"\n >>> {self.name}"