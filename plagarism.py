#Plagarism Checker

from flask import *
app=Flask(__name__)

@app.route('/')
def displayFunc():
	return render_template('index.html', msg="")

@app.route('/check/', methods=['POST','GET'])
def Check():
	result=plagCheck(request.form['string'])
	return render_template('index.html', msg=result)

def plagCheck(mystring):
	fData=""
	with open("data.txt", 'rt') as f:
		for line in f:
			fData=fData+line

	fData=fData.replace('.', '')
	fData=fData.split(' ')

	mystring=mystring.replace('.', '')
	mystring=mystring.split(' ')

	mylist=list(set(mystring) & set(fData))		#Returns only elements which are repeating
	plagCount=len(mylist)

	plagPercent=str(float(plagCount)/len(mystring)*100)
	return plagPercent

if __name__== "__main__":
	app.run()