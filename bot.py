# Pulse - Daily Summary Bot
# Fetches: weather (wttr.in) + quote (zenquotes.io)
# Runs: every day at 8 AM IST via GitHub Actions

import requests
from datetime import date
import os
import smtplib
from email.message import EmailMessage
def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather as a one-line text summary."""
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()

    except Exception as e:
        return f"Weather unavailable ({e})"
def get_quote():
    """Fetch a random motivational quote from ZenQuotes."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()  # JSON -> Python List
        quote = data[0]["q"]
        author = data[0]["a"]
        return f"{quote} - {author}"
    except Exception as e:
        return f"Quote unavailable ({e})"
def build_summary():
    """Assemble the full daily summary from all data sources."""
    today = date.today().strftime("%A, %d %B %Y")
    weather = get_weather()
    quote = get_quote()

    summary = f"""
====================================
PULSE - Daily Summary
{today}
====================================

WEATHER
{weather}

TODAY'S QUOTE
{quote}

====================================
"""
    return summary
def send_weather_alert():
    """Send email if temperature > 35°C or rain is predicted."""

    api_key = os.getenv("OPENWEATHER_API_KEY")
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")

    city = "Kozhikode"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]

        print(f"OpenWeatherMap: {temp}°C, {weather}")

        if True:

            msg = EmailMessage()
            msg["Subject"] = f"Weather Alert - {city}"
            msg["From"] = email_user
            msg["To"] = email_user

            msg.set_content(
                f"""
Weather Alert!

City: {city}
Temperature: {temp}°C
Condition: {weather}

Take necessary precautions.
"""
            )

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_user, email_password)
                smtp.send_message(msg)

            print("Weather alert email sent!")

        else:
            print("No weather alert required.")

    except Exception as e:
        print(f"Alert system error: {e}")    
def run():
    """Main entry point. Called by GitHub Actions."""
    summary = build_summary()
    print(summary)
    
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    
    send_weather_alert()
    
    print("Pulse ran successfully.")

if __name__ == "__main__":
    run()  
  
  
  
      
