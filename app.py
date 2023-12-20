from flask import Flask,request,render_template

app=Flask(__name__)


@app.route('/')
def welcome():
    return "welcome to flask tutorials"

@app.route('/cal',methods=["GET"])
def maths():
    operation=request.json["operation"]
    number1=request.json[number1]
    number2=request.json[number2]
    
    if operation=="add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="divide":
        result=number1/number2   
    else:
        result=number1-number2
    return result             
    

if __name__ == '__main__':
    app.run(debug=True)    