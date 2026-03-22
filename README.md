# Student Tracker

A comprehensive student productivity and expense tracking application built with Streamlit, featuring a modern dark UI and data visualization capabilities.

## Features

- **User Authentication**: Secure registration and login system
- **Expense Tracking**: Log and categorize expenses with detailed records
- **Time Logging**: Track study hours and activities
- **Productivity Analysis**: Calculate productivity scores based on study time and expenses
- **Data Visualization**: Interactive charts and graphs using Plotly
- **Modern UI**: Beautiful dark theme with custom CSS styling

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd student_tracker
```

2. Create a virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install streamlit plotly pandas
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your browser to the provided URL (usually http://localhost:8501)

3. Register a new account or login with existing credentials

4. Start tracking your expenses and study time through the intuitive interface

## Database

The application uses SQLite database (`student.db`) with the following tables:
- `users`: User authentication data
- `expenses`: Expense records with categories
- `time_logs`: Study time and activity logs

The database is automatically created when you first run the application.

## Features Overview

### Dashboard
- View key metrics and KPIs
- Productivity score calculation
- Recent activities overview

### Expense Management
- Add new expenses with categories
- View expense history
- Category-wise expense analysis

### Time Tracking
- Log study hours and activities
- Track productivity over time
- Activity-based time analysis

### Analysis
- Interactive data visualizations
- Productivity trends
- Expense vs. study time correlations

## Dependencies

- Streamlit
- Plotly Express
- Pandas
- SQLite3 (built-in with Python)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.