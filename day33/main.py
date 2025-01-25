import requests
from datetime import datetime
import smtplib
import config


def smtp_sendmail():
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=config.MY_EMAIL, password=config.PASSWORD)
            connection.sendmail(
                from_addr=config.MY_EMAIL,
                to_addrs=config.RECIEVER,
                msg="Look above!\nIss is somewhere on the sky!",
            )
    except:
        print("connection error.")
    else:
        print("E-Mail sent successfully.")


MY_LAT = 50.0614300  # Your latitude
MY_LONG = 19.9365800  # Your longitude



# Your position is within +5 or -5 degrees of the ISS position.


def iss_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude >= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude >= MY_LONG + 5:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False


# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
