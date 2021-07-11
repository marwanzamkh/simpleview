from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SECRET_KEY"] = 'hussam01'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format('b92f40e7a9fe18', '0e03f261', 'us-cdbr-east-04.cleardb.com', 3306, 'heroku_51b533760613fb0')
db = SQLAlchemy(app)
class Vattable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seller_name = db.Column(db.String(200))
    vat_no = db.Column(db.String(80))
    invoice_date = db.Column(db.String(80))
    vat_total =db.Column(db.String(80))
    invoice_total = db.Column(db.String(80))
    barcode=db.Column(db.String(100))

@app.route('/')
def new():

    return render_template("vat.html")
@app.route('/<encoded>', methods=['POST', 'GET'])
def info(encoded):
    print(encoded)
    ty=Vattable.query.first()

    cure = Vattable.query.filter_by(barcode=str(encoded)).first()
    print(cure,ty.barcode)
    if cure:
            r1 = cure.seller_name
            r2 = cure.vat_no
            r3 = cure.invoice_date
            r4 = cure.vat_total
            r5 = cure.invoice_total
            print(r1,r2,r3)
            return render_template("vat.html",r1=r1,r2=r2,r3=r3,r4=r4,r5=r5)

    else:
     print("no barcode")
     return 'The QR Code is not available please contact your vendor'


if __name__ == '__main__':
    app.run()
