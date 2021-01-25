import requests
import bs4
import os
'''
Please run this program in Windows if possible, as I am unfamiliar with directories and paths in Linux/MacOS 
and have only considered Windows functionality

Also, a few links on the pages have been left out, as I elected to remove the ones causing erros or not functioning correctly
'''

#Getting the desktop path for the user running the program allowing it to be run on remote systems as well
parent_dir= os.environ["HOMEPATH"] + r'\Desktop'

#Making the folder for the articles
directory1="India"
path1=os.path.join(parent_dir, directory1)
os.mkdir(path1)

#Crawling the page for articles
url1="https://timesofindia.indiatimes.com/india"
mainsource1=requests.get(url1)
mainsource1=bs4.BeautifulSoup(mainsource1.text, features="html.parser")
urlsoup1=mainsource1.find_all('span',{'class':'w_tle'})
for element in urlsoup1:
    if element.a!=None: #To prevent any random errors
        yoink=element.a.get('href')
        if "/videos/" not in yoink and "http" not in yoink and "/india/" in yoink: #excluding videos and urls, focusing only on the articles
            mainurl="https://timesofindia.indiatimes.com" + yoink
            source=requests.get(mainurl)
            source=bs4.BeautifulSoup(source.text, features="html.parser")
            
            #Getting the date
            date=source.find('div',{'class':'_3Mkg- byline'})
            if date != None: #Removing the pages which follow a different template than the rest, such as the TOI+ articles
                date=date.getText()
                finaldate=date.split(" | ")[-1] #To get the date without the source and "|"
                finaldate=finaldate.split("Updated: ")[-1].strip()
            else:
                continue    
            
            #Getting the title
            title=source.find('div',{'class':'_2NFXP'})
            title=title.find('h1').getText()
            
            #Getting the content of the article
            body=source.find('div',{'class':'ga-headlines'})
            body=body.getText()

            #Prevent naming errors while creating textfiles
            if r'/' not in title and '?' not in title and '\\' not in title and ':' not in title and '*' not in title and '\"' not in title and '<' not in title and '>' not in title and '|' not in title:
                completepath= path1 + r"\\" + title + ".txt" #Placing the textfile inside the folder
                with open(completepath, "w", encoding="utf-8") as file1:
                    file1.write("Title\n")
                    file1.write(title + '\n \n')
                    file1.write("Link\n")
                    file1.write(mainurl + '\n \n')
                    file1.write("Date\n")
                    file1.write(finaldate + '\n \n')
                    file1.write("Text\n")
                    file1.write(body + '\n \n')
                    file1.close()
            else:
                continue        
    else:
        continue            

directory2="World"
path2=os.path.join(parent_dir, directory2)
os.mkdir(path2)
url2="https://timesofindia.indiatimes.com/world"
mainsource2=requests.get(url2)
mainsource2=bs4.BeautifulSoup(mainsource2.text, features="html.parser")
urlsoup2=mainsource2.find_all('span',{'class':'w_tle'})
for element in urlsoup2:
    if element.a!=None:
        yoink=element.a.get('href')
        if "/videos/" not in yoink and "http" not in yoink and "/world/" in yoink:
            mainurl="https://timesofindia.indiatimes.com" + yoink
            source=requests.get(mainurl)
            source=bs4.BeautifulSoup(source.text, features="html.parser")
            
            
            date=source.find('div',{'class':'_3Mkg- byline'})
            if date != None:
                date=date.getText()
                finaldate=date.split(" | ")[-1]
                finaldate=finaldate.split("Updated: ")[-1].strip()
            else:
                continue    
            
            title=source.find('div',{'class':'_2NFXP'})
            title=title.find('h1').getText()
            
            body=source.find('div',{'class':'ga-headlines'})
            body=body.getText()
            if r'/' not in title and '?' not in title and '\\' not in title and ':' not in title and '*' not in title and '\"' not in title and '<' not in title and '>' not in title and '|' not in title:
                completepath= path2 + r"\\" + title + ".txt"
                with open(completepath, "w", encoding="utf-8") as file1:
                    file1.write("Title\n")
                    file1.write(title + '\n \n')
                    file1.write("Link\n")
                    file1.write(mainurl + '\n \n')
                    file1.write("Date\n")
                    file1.write(finaldate + '\n \n')
                    file1.write("Text\n")
                    file1.write(body + '\n \n')
                    file1.close()
            else:
                continue        
    else:
        continue            

directory3="Business"
path3=os.path.join(parent_dir, directory3)
os.mkdir(path3)
url3="https://timesofindia.indiatimes.com/business"
mainsource3=requests.get(url3)
mainsource3=bs4.BeautifulSoup(mainsource3.text, features="html.parser")
urlsoup3=mainsource3.find_all('span',{'class':'w_tle'})
for element in urlsoup3:
    if element.a!=None:
        yoink=element.a.get('href')
        if "/videos/" not in yoink and "http" not in yoink and "/business/" in yoink:
            mainurl="https://timesofindia.indiatimes.com" + yoink
            source=requests.get(mainurl)
            source=bs4.BeautifulSoup(source.text, features="html.parser")

            date=source.find('div',{'class':'_3Mkg- byline'})
            if date != None:
                date=date.getText()
                finaldate=date.split(" | ")[-1]
                finaldate=finaldate.split("Updated: ")[-1].strip()
            else:
                continue    
                
            
            title=source.find('div',{'class':'_2NFXP'})
            title=title.find('h1').getText()
            
            
            body=source.find('div',{'class':'ga-headlines'})
            body=body.getText()
            if r'/' not in title and '?' not in title and '\\' not in title and ':' not in title and '*' not in title and '\"' not in title and '<' not in title and '>' not in title and '|' not in title:
                completepath= path3 + r"\\" + title + ".txt"
                with open(completepath, "w", encoding="utf-8") as file1:
                    file1.write("Title\n")
                    file1.write(title + '\n \n')
                    file1.write("Link\n")
                    file1.write(mainurl + '\n \n')
                    file1.write("Date\n")
                    file1.write(finaldate + '\n \n')
                    file1.write("Text\n")
                    file1.write(body + '\n \n')
                    file1.close()
            else:
                continue
    else:
        continue                


directory4="Homepage"
path4=os.path.join(parent_dir, directory4)
os.mkdir(path4)
url4="https://timesofindia.indiatimes.com"
mainsource4=requests.get(url4)
mainsource4=bs4.BeautifulSoup(mainsource4.text, features="html.parser")
urlsoup4=mainsource4.find_all('span',{'class':'w_tle'})
for element in urlsoup4:
    if element.a!=None:
        yoink=element.a.get('href')
        if "/videos/" not in yoink and "http" not in yoink:
            mainurl="https://timesofindia.indiatimes.com" + yoink
            source=requests.get(mainurl)
            source=bs4.BeautifulSoup(source.text, features="html.parser")

            date=source.find('div',{'class':'_3Mkg- byline'})
            if date != None:
                date=date.getText()
                finaldate=date.split(" | ")[-1]
                finaldate=finaldate.split("Updated: ")[-1].strip()
            else:
                continue    
                
            
            title=source.find('div',{'class':'_2NFXP'})
            title=title.find('h1').getText()
            
            
            body=source.find('div',{'class':'ga-headlines'})
            body=body.getText()
            if r'/' not in title and '?' not in title and ':' not in title and '*' not in title and '\"' not in title and '<' not in title and '>' not in title and '|' not in title:
                completepath= path4 + r"\\" + title + ".txt"
                with open(completepath, "w", encoding="utf-8") as file1:
                    file1.write("Title\n")
                    file1.write(title + '\n \n')
                    file1.write("Link\n")
                    file1.write(mainurl + '\n \n')
                    file1.write("Date\n")
                    file1.write(finaldate + '\n \n')
                    file1.write("Text\n")
                    file1.write(body + '\n \n')
                    file1.close()
            else:
                continue    
    else:
        continue            


