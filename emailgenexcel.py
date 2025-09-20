import os
import google.generativeai as genai
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASS = os.getenv("GMAIL_APP_PASSWORD")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_email(topic, recipient_info):
    prompt = f"Write a professional email about '{topic}' to {recipient_info}. Keep it concise and polite."
    response = model.generate_content(prompt)
    return response.text

def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        print(f"✅ Email sent successfully to {recipient}!")
    except Exception as e:
        print(f"❌ Failed to send email to {recipient}: {e}")

if __name__ == "__main__":
    print("💡 Email Generator + Sender\n")
    
    topic = input("Enter the topic of the email: ")
    file_path = input("Enter path to contacts file (CSV or Excel): ")

    # Read contacts file
    try:
        if file_path.endswith(".csv"):
            contacts = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            contacts = pd.read_excel(file_path)
        else:
            print("❌ Unsupported file type. Use CSV or Excel (.xlsx).")
            exit()
    except Exception as e:
        print(f"❌ Failed to read file: {e}")
        exit()

    drafts = []
    print("\n📧 Generating drafts for preview...\n")
    for index, row in contacts.iterrows():
        name = row.get("Name", "")
        email = row.get("Email", "")
        company = row.get("Company", "")
        position = row.get("Position","")
        recipient_info = f"to {name} from the {company} for the {position}" if company else name
        
        draft = generate_email(topic, recipient_info)
        drafts.append((email, draft))
#can delete if not needed
        print(f"--- Draft for {email} ---")
        print(draft)
        print("\n------------------------\n")

    confirm = input("Do you want to send these emails? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("❌ Sending cancelled.")
        exit()
        
    for email, draft in drafts:
        send_email(f"Regarding: {topic}", draft, GMAIL_USER, email, GMAIL_PASS)
