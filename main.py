"""
Created on Sun July 05 2020
@author: BhagiraTh Desani
@discription: Provides Notification For Coronavirus(COVID-19) Cases Information as well as your computer will keep notifying you from time to time.

"""

from plyer import notification
import requests 
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "/* Add Path */",
        timeout = 6
    )

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        HtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(HtmlData, 'html.parser')
        # print(soup.prettify())
        DataStr = ""

        for tr in soup.find_all('tbody')[0].find_all('tr'):
            DataStr += (tr.get_text())
        DataStr = DataStr[1:]
        itemList = DataStr.split('\n\n')

        states = ['Gujarat','Delhi','Maharashtra','Rajasthan','Punjab']
        for item in itemList[0:35]: 
            dataList = item.split('\n')

            if dataList[1] in states:
                print(dataList)

                n_Title = "Cases of COVID-19"
                n_Text = f"State : {dataList[1]} \nActive Cases : {dataList[2]} \nDischarged Cases : {dataList[3]} \nDeaths : {dataList[4]}"
                notifyMe(n_Title , n_Text)
                time.sleep(5)
        time.sleep(60)        

        
