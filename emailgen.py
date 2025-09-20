import os
import google.generativeai as genai
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

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
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    print("💡 Email Generator and Sender\n")
    
    topic = input("Enter the topic of the email: ")
    recipient_info = input("Enter recipient information : ")
    
    draft = generate_email(topic, recipient_info)
    print("\n📧 Generated Email Draft:\n")
    print(draft)

    send_now = input("\nDo you want to send this email? (yes/no): ").strip().lower()
    if send_now == "yes":
        recipient_email = input("Enter recipient email address: ")
        subject = f"Regarding: {topic}"
        send_email(subject, draft, GMAIL_USER, recipient_email, GMAIL_PASS)
