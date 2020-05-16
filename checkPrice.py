import requests # we can access a URL and pull out the actuall data
from bs4 import BeautifulSoup # we can parse the page and pull out important information
import smtplib

def checkPrice():
    URL = 'https://www.amazon.ca/Sony-ILCE7M2K-Mirrorless-28-70mm-Compact/dp/B00PX8CNCM/ref=sr_1_2?keywords=sony+a7&qid=1585195185&sr=8-2'

    # stores the information about the browser
    headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

    # returns all the data from the website, i/e the particular web page or URL
    page = requests.get(URL,headers=headers)

    # you get all the html content for all that specified url that can be accesses for extracting infromation
    soup = BeautifulSoup(page.content,'html.parser')

    #print(soup.prettify()) 
    # we have the html content in soup variable so now we will find the title of the product that we want to buy
    title = soup.find(id='productTitle').get_text()
    title = title.strip()
    print("The product title is " + title)

    # extrat the price
    price = soup.find(id='priceblock_ourprice').get_text()

    # all the steps to conver the price into float
    extractedPrice = price[5:10]
    tempPrice = list(extractedPrice)
    tempPrice[1] = '.'
    stringPrice = ''.join(tempPrice)
    convertedPrice = float(stringPrice)
    print(convertedPrice)
    # after this step the price has been sucessfully converetd to float

    if(convertedPrice < 1.700):
        sendEmail() 

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() # establishes the connection between the two
    server.starttls() # encrypts our connection
    server.ehlo()

    server.login('email','password')
    subject = "The price fell down"
    body = "Check the link below to place your order https://www.amazon.ca/Sony-ILCE7M2K-Mirrorless-28-70mm-Compact/dp/B00PX8CNCM/ref=sr_1_2?keywords=sony+a7&qid=1585195185&sr=8-2"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('From','To',msg)
    print("Email has been successfullt sent")
    server.quit()

checkPrice()


