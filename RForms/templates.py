from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from models import db
from models import Form
from models import Field
from models import Answer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import flag_modified
from settings import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://semusr:12345@localhost/radiusforms'
db = SQLAlchemy(app)

@app.route("/")
def prin():

    return "Helsddd World!"

@app.route("/name")
def name():
	parm = request.args.get('names', 'no existe valor')
	return 'El señor es {}'.format(parm)

@app.route("/plantilla")
def plantilla():

	return render_template('create_form.html')

@app.route("/New_form", methods = ['GET', 'POST'])
def New_form():
    if request.method == 'POST':
        nameF = request.form['form_name']
        nameA = request.form['area']
        print(nameF)
        print(nameA)
        #f = Form(name=request.form['form_name'],detail=request.form['area'])
        f = Form(name= request.form['form_name'],detail=request.form['detail'],estatus="I")
        db.session.add(f)
        db.session.commit()

        datos=request.form['area']
        print (datos)
        campos = datos.split(';')
        for campo in campos:
            info = campo.split(':')
            if len(info)>1:
                listado = f.id
                camp = Field(form_id = f.id,name= info[0].replace(' ','_'),tipe=info[1],label=info[2],detail=info[3].replace(' ','_'))
                db.session.add(camp)
                db.session.commit()


        return redirect('/plantilla')

@app.route("/list_forms", methods = ['GET', 'POST'])
def list_forms():
    data=[]
    forms = Form.query.all()
    for f in forms:
        print(f)
        print(f.name,f.detail)
        data.append({"id":f.id,"name":f.name,"estatus":f.estatus})

    return render_template('show_forms.html',data=data)

@app.route("/view_form", methods = ['GET', 'POST'])
def view_form():
    data=[]

    forms = Form.query.get(request.form['id_form'])
    fields = Field.query.filter_by(form_id=request.form['id_form'])
    print("5555555555555555")
    for f in fields:
        print(f.id)
        print(f.name)
        print(f.tipe)
        print(f.label)
        data.append({"id":f.id,"name":f.name,"label":f.label,"type":f.tipe})

    return render_template('view_form.html',data=data,form=forms)

@app.route("/save_info", methods = ['GET', 'POST'])
def save_info():

    datos=request.form['res']
    print (datos)
    campos = datos.split(';')
    for campo in campos:
        info = campo.split(':')
        if len(info)>1:
            answers = Answer(serial= request.form['id_form'],field_id=info[0],data=info[1].replace(' ','_'))
            db.session.add(answers)
            db.session.commit()

    return redirect('/list_forms')

@app.route("/update_status", methods = ['GET', 'POST'])
def update_status():
    data=[]
    forms = Form.query.all()
    #import pdb; pdb.set_trace()
    f = Form.query.get(request.form['Id_Status'])
    #fields = Field.query.filter_by(form_id=request.form['id_form'])
    session = db.session
    session.autocommit = True
    for i in forms :
        if(i.id == f.id):
            f.estatus = "A"
            session.merge(f)
        else:
            i.estatus = "I"
            session.merge(i)
        session.close()
    return redirect('/list_forms')

@app.route("/delete_form", methods = ['GET', 'POST'])
def delete_form():
    data=[]
    session = db.session
    session.autocommit = True
    fdel = Form.query.get(request.form['textborrar'])
    print(fdel)

    #session.query(Form).filter(Form.id==6).delete()

    obj=session.query(Form).filter(Form.id==request.form['textborrar']).first()

    fields = Field.query.filter_by(form_id=request.form['textborrar'])


    for fi in fields:
        data.append(fi.id)

        idf = fi.id
        #cam = session.query(Field).filter_by(form_id=3)
        #session.query(Field).filter(Field.form_id==fi.id).delete()
        print("555555555555555555")

        #print(cam)
        session.delete(fi)
        session.commit(fi)
    print(data)

    #session.delete(obj)

    #session.delete(fdel)
    session.close()
    return redirect('/list_forms')

@app.route("/form_act")
def form_act():
    data=[]
    forms = Form.query.filter_by(estatus = 'A').first()
    fields = Field.query.filter_by(form_id=forms.id)

    for f in fields:
        print(f)
        print(f.id)
        print(f.name)
        print(f.tipe)
        print(f.label)
        data.append({"id":f.id,"name":f.name,"label":f.label,"type":f.tipe})

    return render_template('form_activo.html',data=data,form=forms)


if __name__ == '__main__':
    db.init_app(app)
    app.jinja_env.auto_reload =  True
    app.config [ ' TEMPLATES_AUTO_RELOAD ' ] =  True
    app.run(debug = True, port= 8080)
