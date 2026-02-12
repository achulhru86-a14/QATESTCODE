from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this_in_production'

# Simple in-memory user database (in production, use a real database)
users = {
    'user@example.com': generate_password_hash('password123'),
    'admin@example.com': generate_password_hash('admin123')
}

# Decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'user_email' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validate user credentials
        if email in users and check_password_hash(users[email], password):
            session['user_email'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid email or password')
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # BUG: Missing cache-control headers allow browser to cache this protected page
    return render_template('dashboard.html', user_email=session.get('user_email'))

@app.route('/account')
@login_required
def account():
    # BUG: No cache-control headers - page will be cached by browser
    # This allows the page to be viewed after logout using browser back button
    return render_template('account.html', user_email=session.get('user_email'))

@app.route('/orders')
@login_required
def orders():
    # BUG: Missing cache-control headers allow browser to cache sensitive order data
    # User can access this after logout by pressing back button
    orders_data = [
        {'id': 'ORD001', 'date': '2025-12-15', 'total': '$250.00', 'status': 'Delivered'},
        {'id': 'ORD002', 'date': '2025-12-20', 'total': '$180.50', 'status': 'Processing'},
        {'id': 'ORD003', 'date': '2026-01-05', 'total': '$425.75', 'status': 'Shipped'}
    ]
    return render_template('orders.html', user_email=session.get('user_email'), orders=orders_data)

@app.route('/logout')
def logout():
    # BUG: Session is cleared, but no cache-control headers are set
    # Browser cached content remains accessible via back button
    # Session cookie is not properly invalidated with secure flags
    session.pop('user_email', None)
    return redirect(url_for('login'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
