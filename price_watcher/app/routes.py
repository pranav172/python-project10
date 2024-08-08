from flask import render_template, request, redirect, url_for, flash
from app import create_app
from app.models import add_product
from app.price_checker import check_prices

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        level = float(request.form['level'])
        add_product(link, level)
        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/check_prices')
def manual_check_prices():
    check_prices()
    flash('Prices checked manually!', 'info')
    return redirect(url_for('index'))