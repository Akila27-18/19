from flask import Flask, render_template, flash, redirect, url_for
from forms import DonationForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        name = form.name.data
        amount = form.amount.data
        cause = form.cause.data
        flash(f"Thank you {name}! You donated ₹{amount} to {cause}", "success")
        return redirect(url_for('donate'))
    return render_template('donate.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
