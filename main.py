try:
    from flask import Flask, request, redirect, render_template
    from flask_sqlalchemy import SQLAlchemy
    from datetime import datetime
    import ipapi ,base64
except:
    import os
    pip=['ipapi','flask','flask_sqlalchemy']
    for i in pip:
        os.system(f'pip install {i}')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your database model
class URLVisit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<URLVisit {self.url} from {self.email} at {self.timestamp}>'

# Routes
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/r', methods=['GET'])
def redirect_url():
    new_url = request.args.get('u')
    email = request.args.get('em')
    try:
        # Attempt to decode the email from base64
        email = base64.b64decode(email).decode('utf-8')
    except Exception as e:
        pass
    try:
        # Attempt to decode the email from base64
        new_url = base64.b64decode(new_url).decode('utf-8')
    except Exception as e:
        pass
    country = ipapi.location(request.remote_addr, output='country_name')# Replace with actual header for country
    if new_url and email:
        # Save to database
        visit = URLVisit(url=new_url, email=email, country=country)
        db.session.add(visit)
        db.session.commit()

        return redirect(new_url)
    else:
        return 'Missing parameters: u or email'

@app.route('/dashboard/<path:new_url>')
def dashboard(new_url):
    # Ensure authentication for dashboard access
    # For simplicity, let's assume new_url is used as a password (not secure, just for demonstration)
    visits = URLVisit.query.filter_by(url=new_url).all()
    return render_template('dashboard.html', visits=visits)
# Create all database tables within the application context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0',port='5000')
