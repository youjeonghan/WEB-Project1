from pybo import db

# 모델 클래스의 각각의 속성은 db.Column을 사용하여 생성할 수 있다.
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))   # ondelete=CASCADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미
    # question 속성은 답변모델에서 질문모델을 참조하기 위해서 추가된 속성이다. 즉, answer.question.subject 처럼 답변 모델 객체(answer)를 통해서 질문모델 객체(question)를 참조할 수 있게 된다.
    # 이를 위해서는 db.relationship 을 이용하여 속성을 추가해 주어야 한다. db.relationship에서 사용된 backref 속성은 answer.question.subject 와는 반대로 질문에서 답변모델을 참조하기 위해서 사용되는 속성이다.
    # 하나의 질문에는 여러개의 답변이 작성될 수 있는데 어떤 질문에 해당되는 객체가 a_question 이라면 이 질문에 작성된 답변들을 참조하기 위해서 a_question.answer_set 과 같이 사용할 수 있다.
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)