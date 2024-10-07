

# Flask URL Tracker

## Overview

The **Flask URL Tracker** is a simple web application that tracks visits to specified URLs. Users can redirect to a URL and the application logs the visit details, including the user's email, location, and the timestamp of the visit. This application uses Flask as the web framework and SQLite as the database.

## Features

- **URL Redirection**: Redirects users to specified URLs while logging visit details.
- **Visit Logging**: Logs each visit with the URL, user's email, country of origin, and timestamp.
- **Dashboard**: Provides a simple dashboard to view visit logs for each URL.
- **Automatic Dependency Installation**: Automatically installs required packages if not already available.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Flask-SQLAlchemy**: An ORM for easier database interactions.
- **SQLite**: Lightweight database for storing visit logs.
- **ipapi**: A service for retrieving location information based on IP address.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system.

### Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/yourusername/flask-url-tracker.git
cd flask-url-tracker
```

### Install Dependencies

Run the application, and it will automatically install any missing dependencies. You can also manually install them using pip:

```
pip install flask flask_sqlalchemy ipapi
```

## Usage

### Running the Application

To start the Flask application, run the following command:

```
python app.py
```

The application will start on `http://0.0.0.0:5000/`.

### Accessing the Application

1. **Index Page**: Navigate to the root URL (`/`) to see a welcome message.
2. **URL Redirection**: Use the following format to redirect:
   ```
   http://<your-server-ip>:5000/r?u=<base64_encoded_url>&em=<base64_encoded_email>
   ```
   - Replace `<base64_encoded_url>` with the base64 encoded version of your target URL.
   - Replace `<base64_encoded_email>` with the base64 encoded version of the user's email.

3. **Dashboard**: Access the dashboard using:
   ```
   http://<your-server-ip>:5000/dashboard/<url>
   ```
   This will display the visit logs for the specified URL. 

### Example

To redirect to `https://example.com` with an email `user@example.com`, you would encode the URL and email in base64:

- Base64 encoded URL: `aHR0cHM6Ly9leGFtcGxlLmNvbQ==`
- Base64 encoded Email: `dXNlckBleGFtcGxlLmNvbQ==`

Then, use the following URL:

```
http://<your-server-ip>:5000/r?u=aHR0cHM6Ly9leGFtcGxlLmNvbQ==&em=dXNlckBleGFtcGxlLmNvbQ==
```

## Database

The application uses SQLite to store visit logs. The database file `url_tracker.db` will be created in the project directory upon the first run.

## Contact

For any inquiries or collaboration on this project, feel free to reach out:

- **Telegram**: [Nouredine](https://t.me/nouredinekn)

