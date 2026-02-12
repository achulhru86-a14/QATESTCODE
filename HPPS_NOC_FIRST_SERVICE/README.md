# Login Web Application

A simple Flask-based web application with user authentication, login, and logout functionality.

## Features

- **User Authentication**: Secure login with email and password
- **Session Management**: User sessions with login required decorator
- **Password Hashing**: Passwords are hashed using Werkzeug security
- **Responsive Design**: Mobile-friendly UI
- **Dashboard**: Welcome dashboard for authenticated users
- **Error Handling**: 404 error page for missing resources

## Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── login.html        # Login page
│   ├── dashboard.html    # Dashboard page
│   └── 404.html          # Error page
└── static/
    └── style.css         # Stylesheet
```

## Installation

1. Make sure you have Python 3.7+ installed
2. Clone or download this project
3. Navigate to the project directory
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Open PowerShell or Command Prompt
2. Navigate to the project directory
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## Demo Credentials

You can log in with these test accounts:

**Account 1:**
- Email: `user@example.com`
- Password: `password123`

**Account 2:**
- Email: `admin@example.com`
- Password: `admin123`

## How It Works

1. **Login Page**: Users enter their email and password
2. **Authentication**: Credentials are verified against the user database
3. **Session Creation**: Upon successful login, a session is created
4. **Dashboard**: Users can view their personalized dashboard
5. **Logout**: Users can click logout to end their session

## Security Notes

⚠️ **Important for Production:**
- Change the `secret_key` in `app.py` to a strong, unique value
- Use a proper database (PostgreSQL, MySQL, etc.) instead of in-memory storage
- Implement HTTPS/SSL encryption
- Add CSRF protection
- Use environment variables for sensitive data
- Implement rate limiting on login attempts
- Add email verification
- Use proper session management strategies

## Features You Can Add

- User registration
- Password reset functionality
- User profile page
- Database integration (SQLAlchemy)
- Email verification
- Two-factor authentication
- User roles and permissions
- Activity logging
- Remember me functionality
- Social media login integration

## Technologies Used

- **Flask**: Web framework
- **Werkzeug**: Security utilities
- **HTML5**: Markup
- **CSS3**: Styling
- **Python**: Backend language

## License

This project is open source and available for educational purposes.
