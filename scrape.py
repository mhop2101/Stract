#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import requests
from bs4 import BeautifulSoup
import datetime
import random
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"
#pandas.options.display.max_rows = 500


# In[2]:
url     = "https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|1||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||"
strfrmt = 'https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|{}||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||'

def get_avg_time(url):
    r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    content = r.content
    soup = BeautifulSoup(content,"html.parser")
    pageNumbers = soup.find("span",{"id":"lblNumInm"})
    pageNumbers = pageNumbers.text[0:-1].replace(",","")
    pageNumbers = int(pageNumbers)
    pageNumbers = int(pageNumbers/32)+4
    # 25 ====> 557
    # pN ====> X
    seconds = (pageNumbers * 557) / 25
    taken_time = str(datetime.timedelta(seconds=seconds)).split(":")
    finish_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
    # UTC-5
    return taken_time , str(finish_time)


def scrape(url,strfrmt,name):
    avoid_errors=False
    print("Scrape URL")
    print(url)
    # https://www.fincaraiz.com.co/apartamento-casa-apartaestudio-lote/venta/bella-suiza/bogota/?ad=30|1||||1||8,9,22,2|||67|3630001|||||||||||||||||||1||griddate%20desc|||bella+suiza|-1||
    # r = requests.get("https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|1||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    source_url = "https://www.fincaraiz.com.co"

    header1 = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    header2 = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    headers = [header1,header2]
    r = requests.get(url, headers=random.choice(headers))
    content = r.content
    soup = BeautifulSoup(content,"html.parser")
    pageNumbers = soup.find("span",{"id":"lblNumInm"})
    pageNumbers = pageNumbers.text[0:-1].replace(",","")
    pageNumbers = int(pageNumbers)
    pageNumbers = int(pageNumbers/32)+4
    prices_list = []
    names_list = []
    areas_list = []
    rooms_list = []
    url_list = []
    m2_list = []
    status_list = []
    sect_list = []
    bathrooms_list = []
    garages_list = []
    antique_list = []
    floorNumber_list = []
    adminvalue_list = []
    state_list = []
    print(pageNumbers)


    # In[3]:


    for i in range(2,pageNumbers):
        r = requests.get(strfrmt.format(i), headers=random.choice(headers))
        content = r.content
        soup = BeautifulSoup(content,"html.parser")
        divAdverts = soup.find("div",{"id":"divAdverts"})
        medias = divAdverts.find_all("li",{"class":"media"})
        for i in range(0,len(medias)):
            string = str(medias[i])
            var = string[55:].split("'")
            if var[0] == "ascript:window.location=":
                print("I refuse to append proyects")
            else:
                url_list.append(source_url+var[0])

    # In[5]:


    progress = 1
    total = len(url_list)

    for url in url_list:
        tries = 0
        r = requests.get(url,headers=random.choice(headers))
        content = r.content
        soup = BeautifulSoup(content,"html.parser")

        try:
            bathrooms = soup.find("span",{"class":"advertBaths"})
            bathrooms_list.append(bathrooms.text.replace(" ","").replace("\r","").replace("\n","").replace("Baños","").replace(":",""))

        except AttributeError:
            bathrooms_list.append("0")
            print("0 baths")

        try:
            garages = soup.find("span",{"class":"advertGarages"})
            garages_list.append(garages.text.replace(" ","").replace("\r","").replace("\n","").replace("Parqueaderos","").replace(":",""))

        except AttributeError:
            garages_list.append("0")
            print("0 garages")

        try:
            rooms = soup.find("span",{"class":"advertRooms"})
            rooms_list.append(rooms.text.replace(" ","").replace("\r","").replace("\n","").replace("Habitaciones","").replace(":",""))
        except AttributeError:
            garages_list.append("0")
            print("0 rooms")

        try:
            areas = soup.find("span",{"class":"advertSurface"})
            areas_list.append(areas.text.replace(" ","").replace("\r","").replace("\n","").replace(":",""))
        except AttributeError:
            garages_list.append("0")
            print("0 rooms")
        try:
            prices = soup.find("div",{"class":"price"})
            prices_list.append(prices.text.replace("\n",""))
        except AttributeError:
            prices_list.append("0")
            print("0 prices")
        try:
            title = soup.find("h1")
            names_list.append(title.text)
        except AttributeError:
            names_list.append("0")
            print("0 names")


        try:
            boxcube = soup.find("ul",{"class":"boxcube"})
            add_info = boxcube.find_all("li")

            for item in add_info:
                if item.text.replace("\r","").replace("\n","").replace(" ","")[0:8] == 'Preciom²':
                    print(item.text.replace("\r","").replace("\n","").replace(" ","")[9:])
                    m2_list.append(item.text.replace("\r","").replace("\n","").replace(" ","")[9:])

            for item in add_info:
                if item.text.replace("\r","").replace("\n","").replace(" ","")[0:7] == "Estrato":
                    print(item.text.replace("\r","").replace("\n","").replace(" ","")[8:])
                    status_list.append(item.text.replace("\r","").replace("\n","").replace(" ","")[8:])

            for item in add_info:
                if item.text.replace("\r","").replace("\n","").replace(" ","")[0:6] == "Sector":
                    print(item.text.replace("\r","").replace("\n","").replace(" ","")[7:])
                    sect_list.append(item.text.replace("\r","").replace("\n","").replace(" ","")[7:])

            for item in add_info:
                if item.text.replace("\r","").replace("\n","").replace(" ","")[0:10] == "Antigüedad":
                    print(item.text.replace("\r","").replace("\n","").replace(" ","")[11:])
                    antique_list.append(item.text.replace("\r","").replace("\n","").replace(" ","")[11:])

            for item in add_info:
                if item.text.replace("\r","").replace("\n","").replace(" ","")[0:6] == "PisoNo":
                    print(item.text.replace("\r","").replace("\n","").replace(" ","")[7:])
                    floorNumber_list.append(item.text.replace("\r","").replace("\n","").replace(" ","")[7:])

            for item in add_info:
                if item.text.replace("\r","").replace("\n","").replace(" ","")[0:5] == "Admón":
                    holder = item.text.replace("\r","").replace("\n","").replace(" ","")[6:]
                    holder = holder.split("Estrato")
                    print(holder[0])
                    adminvalue_list.append(holder[0])

            for item in add_info:
                if item.text.replace("\r","").replace("\n","").replace(" ","")[0:6] == "Estado":
                    print(item.text.replace("\r","").replace("\n","").replace(" ","")[7:])
                    state_list.append(item.text.replace("\r","").replace("\n","").replace(" ","")[7:])

            if len(antique_list) != len(sect_list):
                antique_list.append("Sin info")

            if len(floorNumber_list) != len(sect_list):
                floorNumber_list.append("Sin info")

            if len(adminvalue_list) != len(sect_list):
                adminvalue_list.append("Sin info")

            if len(state_list) != len(sect_list):
                state_list.append("Sin info")



            bathroom_lenght = len(bathrooms_list)
            if bathroom_lenght != len(m2_list):
                tries = bathroom_lenght - len(m2_list)
                for i in range(0,tries):
                    m2_list.append("0")


            if bathroom_lenght != len(status_list):
                tries = bathroom_lenght - len(status_list)
                for i in range(0,tries):
                    status_list.append("0")
            print("succesfully added")

        except IndexError:
            sect_list.append("0")
            m2_list.append("")
            status_list.append("0")
            print("0 objects")

        print("bathroom_lenght ",len(bathrooms_list))
        print("m2_lenght ",len(m2_list))
        print("status_lenght",len(status_list))
        print(int((progress/total)*100),"Percent\n\n")
        progress += 1


    # In[43]:

    if avoid_errors == True:
        info = {"Price":prices_list,"Bathrooms":bathrooms_list,"Garages":garages_list,
        "Sector":sect_list,"Estrato":status_list,"Precio_x_Metro":m2_list,"Adminstracion":adminvalue_list,
        "Antigüedad":antique_list,"Estado":state_list,"Piso":floorNumber_list,"URL":url_list}
        df = pandas.DataFrame(data=info)
    else:
        info = {"Titulo":names_list,"Sector":sect_list,"Cuartos":rooms_list,
        "Baños":bathrooms_list,"Garages":garages_list,"Area":areas_list,
        "Estrato":status_list,"Antigüedad":antique_list,"Estado":state_list,
        "Piso":floorNumber_list,"Adminstracion":adminvalue_list,"Price":prices_list,
        "Precio_x_Metro":m2_list,"URL":url_list}
        df = pandas.DataFrame(data=info)



    # In[47]:


    df = df.query('Precio_x_Metro != "0"')


    # In[48]:

    # In[49]:


    export_csv = df.to_csv(name)


    # In[ ]:


if __name__ == "__main__":
    scrape(url,strfrmt)
