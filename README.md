# EmailGen

EmailGen is a Python project that generates professional email drafts using Gemini AI and sends them via Gmail. It supports sending single emails as well as bulk emails from Excel or CSV files.

---

## Features

- Generate professional email drafts using Gemini 1.5 Flash
- Send emails via Gmail SMTP
- Read recipients from Excel (.xlsx) or CSV files
- Preview all drafts before sending
- Safe environment variable handling using `.env`

---

## Project Structure

EmailGen/
│
├── email_generator.py # Single email generator & sender
├── email_generator_excel.py # Bulk email generator with Excel/CSV support
├── requirements.txt # Python dependencies
├── .gitignore # Ignore sensitive files
├── .env.example # Template for API keys and Gmail credentials
└── README.md # Project overview

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/EmailGen.git
cd EmailGen
Install dependencies

pip install -r requirements.txt


Setup environment variables

Copy .env.example to .env:

cp .env.example .env   # Linux/Mac
# or manually copy for Windows


Fill in your Gemini API key and Gmail credentials.

Prepare contacts

For single emails: no extra file needed.

For bulk emails: create a CSV or Excel file with columns Name, Email, Company, Position (Position is optional).

Run the scripts

Single email:

python emailgen.py


Bulk emails:

python emailgenexcel.py


License

This project is open source and free to use.
