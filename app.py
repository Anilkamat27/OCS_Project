from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        role = request.form['role']
        user_id = request.form['user_id']
        password = request.form['password']

        if role.lower() == 'basic':  # Make sure to use lowercase for comparison
            db.insert_user(role, user_id, password)
        elif role.lower() == 'admin':  # Make sure to use lowercase for comparison
            data = db.get_admin_data()
            return render_template('admin.html', data=data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
