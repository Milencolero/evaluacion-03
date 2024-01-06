from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def formnotas():
    if request.method == 'POST':
        estado = ''
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        numero3 = float(request.form['numero3'])
        asistencia = float(request.form['asistencia'])
        resultado = (numero1+numero2+numero3)/3
        if asistencia >= 75 and resultado >= 40.0:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'
        return render_template('ejercicio1.html', resultado=resultado, numero1=numero1, numero2=numero2,numero3=numero3,estado=estado)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def contarcaracteres():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        conta1 = len(nombre1)
        conta2 = len(nombre2)
        conta3 = len(nombre3)
        dato = 0
        lista=[conta1,conta2,conta3]
        resultado= max(lista)
        if resultado == conta1:
            dato = nombre1
        elif resultado == conta2:
            dato = nombre2
        elif resultado == conta3:
            dato = nombre3
        return render_template('ejercicio2.html', nombre1=nombre1,nombre2=nombre2,nombre3=nombre3,conta1=conta1,conta2=conta2,conta3=conta3,resultado=resultado,dato=dato)
    return render_template('ejercicio2.html')
if __name__ == '__main__':
    app.run(debug=True)