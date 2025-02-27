from flask import Flask, render_template , url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong , try again!'

def write_to_csv(data):
    with open('database.csv',  newline='' , mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', qouting=csv.QOUTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
if __name__ == "__main__":
    app.run()
    