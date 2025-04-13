from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'some_random_secret_key'

@app.route('/first_form', methods=['GET', 'POST'])
def first_form():
    if request.method == 'POST':
        # Store the entire form or specific fields in the session
        session['name'] = request.form.get('name')
        session['email'] = request.form.get('email')
        
        return redirect(url_for('second_form'))
    
    return render_template('first_form.html')
@app.route('/second_form', methods=['GET', 'POST'])
def second_form():
    if request.method == 'POST':
        # Process the second form here
        # ...
        return redirect(url_for('success'))  # or wherever you want
    
    # Get the stored values from the session
    stored_name = session.get('name')
    stored_email = session.get('email')

    # Render the template with the prefilled data
    return render_template('second_form.html', name=stored_name, email=stored_email)
if __name__=="__main__":
    app.run(debug=True)
    
