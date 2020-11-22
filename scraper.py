import requests
from bs4 import BeautifulSoup 
import smtplib #simple mail protocol to send mail
import time


URL ='https://www.amazon.in/Redmi-Note-Pro-Interstellar-Snapdragon/dp/B077PWBC78/ref=sr_1_1?crid=2SZKRTLGK9J8M&dchild=1&keywords=redmi+note+9+pro&qid=1606038677&sprefix=red%2Caps%2C338&sr=8-1'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36' }


def check_price():
    page=requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()

    price_range = soup.find(id='priceblock_ourprice').get_text()
    price_range = price_range.replace(',','')
    
    converted_price = float(price_range[1:7])
    if(converted_price < 12500):
        send_mail()


def send_mail():
    #connection with our connection and gmail connection
    server = smtplib.SMTP('smtp.gmail.com',587) # google smtp
    server.ehlo() #Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    server.starttls() # encrpyt our connection
    server.ehlo()

    server.login('gauravkumar.gk818@gmail.com','googleapppassword') # This password is app password generated to act as gmail password through google. You have to generate using app password gmail

    subject = 'Price fell down!!'
    body='Check the amazon link for the item whose price went down https://www.amazon.in/Redmi-Note-Pro-Interstellar-Snapdragon/dp/B077PWBC78/ref=sr_1_1?crid=2SZKRTLGK9J8M&dchild=1&keywords=redmi+note+9+pro&qid=1606038677&sprefix=red%2Caps%2C338&sr=8-1'

    msg=f"Subject:{subject}\n\n{body}" # msg to be sent in the mail

    # sendmail is the function to send mail from the particular connection to who we want to send it
    server.sendmail(
        'from', #from is to be replaced by the person who wants to send the mail
        'to', # to will be replaced by the person who will recieve the mail
        msg
    )
    print('Hey! Email has been sent')
    server.quit

#while(True):
    check_price()
#   time.sleep(60 * 60 * 24)
