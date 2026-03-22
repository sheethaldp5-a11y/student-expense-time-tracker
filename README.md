# Student Tracker

A comprehensive web application built with Streamlit for students to track their expenses, time logs, and productivity metrics. Features a modern dark theme with beautiful gradients and interactive dashboards.

## Features

- **User Authentication**: Secure registration and login system
- **Expense Tracking**: Log expenses with categories, amounts, dates, and times
- **Time Logging**: Track time spent on various activities
- **Analytics Dashboard**: View productivity scores and expense insights with interactive charts
- **Modern UI**: Dark theme with gradient backgrounds and smooth animations
- **SQLite Database**: Local data storage for user data and logs

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd student-tracker
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install streamlit pandas plotly
```

## Database Setup

The application uses SQLite database (`student.db`) which is created automatically when you run the app for the first time. The database includes the following tables:

- `users`: User authentication data
- `expenses`: Expense tracking records
- `time_logs`: Time logging records

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your browser to `http://localhost:8501`

3. Register a new account or login with existing credentials

4. Navigate through the different sections:
   - **Dashboard**: View overview and productivity metrics
   - **Add Expense**: Log new expenses
   - **Log Time**: Record time spent on activities
   - **Expense Insights**: Analyze spending patterns

## Dependencies

- streamlit
- pandas
- plotly

## Project Structure

```
student_tracker/
├── app.py          # Main Streamlit application
├── auth.py         # Authentication functions
├── database.py     # Database setup and schema
├── expense.py      # Expense management functions
├── time_log.py     # Time logging functions
├── analysis.py     # Data analysis and dashboard functions
├── student.db      # SQLite database (created automatically)
└── README.md       # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).