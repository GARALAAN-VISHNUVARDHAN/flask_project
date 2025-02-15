from flask import Flask,render_template,request
dd=Flask(__name__)
@dd.route('/')
def home():
    return render_template('call.html')
@dd.route('/cal',methods=['post'])
def cal():
    try:
        x=int(request.form['Num1'])
        y=int(request.form['Num2'])
        r=x+y
        return render_template('callr.html',result=r)
    except Exception as e:
        return f'{e}'
if __name__=='__main__':
    dd.run(debug=True)