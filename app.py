from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flashing messages

# Home page with input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and calculation
@app.route('/calculate', methods=['POST'])
def calculate_cpr():
    if request.method == 'POST':
        try:
            # Get first set of performance and cost
            performance1 = float(request.form['performance1'])
            cost1 = float(request.form['cost1'])
            if performance1 <= 0 or cost1 <= 0:
                flash('Performance and cost must be positive numbers for Set 1.', 'error')
                return redirect(url_for('index'))
            cpr1 = performance1 / cost1

            # Get second set of performance and cost (optional)
            performance2 = request.form.get('performance2')
            cost2 = request.form.get('cost2')
            cpr2 = None
            if performance2 and cost2:
                performance2 = float(performance2)
                cost2 = float(cost2)
                if performance2 > 0 and cost2 > 0:
                    cpr2 = performance2 / cost2
                else:
                    flash('Performance and cost must be positive numbers for Set 2.', 'error')
                    return redirect(url_for('index'))

            return render_template('result.html', cpr1=cpr1, cpr2=cpr2)

        except ValueError:
            flash('Please enter valid numbers for performance and cost.', 'error')
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
