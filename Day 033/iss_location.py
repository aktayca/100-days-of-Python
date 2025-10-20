import requests
from datetime import datetime
import smtplib

MY_LAT = 41.008240
MY_LNG = 28.978359
MY_EMAIL = "YourEmail@Here.Com"
MY_PASS = "Your Mail App Password Here"
RECIPIENT = "MailTarget@Here.Com"
DEGREE_OFFSET = 5 #For looser degree matching
UTC_OFFSET = 3 #Because Sunset-Sunrise API returns time in UTC and Turkey is UTC+3


def iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_lat = float(data_iss["iss_position"]["latitude"])
    iss_lng = float(data_iss["iss_position"]["longitude"])

    if (MY_LAT - DEGREE_OFFSET) <= iss_lat <= (MY_LAT + DEGREE_OFFSET) \
    and (MY_LNG - DEGREE_OFFSET) <= iss_lng <= (MY_LNG + DEGREE_OFFSET):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response_ss = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response_ss.raise_for_status()
data_ss = response_ss.json()
sunrise = int(data_ss["results"]["sunrise"].split("T")[1].split(":")[0])+UTC_OFFSET
sunset = int(data_ss["results"]["sunset"].split("T")[1].split(":")[0])+UTC_OFFSET
sunrise %= 24 #In case UTC offset makes it go past the midnight(Potentially for far east, not for TR)
sunset %= 24 #In case UTC offset makes it go past the midnight



def after_sunset():
    time_now = int(str(datetime.now()).split(" ")[1].split(":")[0])
    if time_now >= sunset or time_now<=sunrise:
        return True
    else:
        return False

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password= MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECIPIENT,
                            msg=f"Subject:Kafani kaldirirsan ISS goruyor olabilirsin\nTo:{RECIPIENT}\n\n ISS su an senin lokasyonuna yakin ve gunes yok, o yuzden gorebiliyor olabilirsin")

if iss_overhead() and after_sunset():
    send_mail()
    