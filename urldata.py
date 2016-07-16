import requests
import os
import csv
from bs4 import BeautifulSoup


#This function will go to html page and takes url
#and searchs for ceratin url and downlaods the file
def get_csvfile(get_url):
    try:
        response=requests.get(get_url)
        soup=BeautifulSoup(response.content,'html.parser')
        for link in soup.find_all('a'):
            if "Download to Spreadsheet" in (link.text):
                url=link.get('href')
                #print url
        
                resp = requests.get(url)
                output = open('test.csv', 'wb')
                output.write(resp.content)
                output.close()    

    except requests.exceptions.Timeout:
        print "Timeout"
        sys.exit(0)

    except requests.exceptions.TooManyRedirects:
        print "Too many redirections.Please try with different URL"
        sys.exit(0)
    
    
    return True


