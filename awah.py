from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
    i = 0
    while i<=j:
        print(" "),
        i+=1
def Credit():
    Space(9); print("#####################################")
    Space(9); print("#            AWAH V 1.0             #")
    Space(9); print("#     Scripted by CYBA TIGER        #")
    Space(9); print("#         GHOSTFLEET.ORG            #")
    Space(9); print("#####################################")
def Main():
    Credit()
    url=raw_input("\n\nEnter Site Name \n(ex : example.com or www.example.com ): ")
    injFinder(url)
    finder(url)


def finder(url):
    f = open("link.txt","r");
    link = url
    print("RESULTS=>\n")
    while True:
        sub_link = f.readline()
        if not sub_link:
            break
        req_link = "http://"+link+"/"+sub_link
        req = Request(req_link)
        try:
            response = urlopen(req)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            req_link=req_link.replace('\n',' ')
            a=[]
            for i in a:
                a[i]=req_link

            print a

def injFinder(url):
    import urllib
    import mechanize
    from bs4 import BeautifulSoup
    import re

    br =mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders=[{'User-agent','chrome'}]

    url=url.replace("www.","")
    dork="inurl:php?id= site:"+url
    
    encode=urllib.quote(dork)
    url="http://uk.ask.com/web?q="+ encode

    raw = br.open(url).read()
    soup= BeautifulSoup(raw)
    divs=soup.findAll('div')

    a= re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(divs))
    print "\n\n THE IMPORTANT LINKS FOUND IN THE SITE ARE: \n"
    b=len(a)
    for i in range(13,b):
        c=a[i]
            
        if i==15:
            break
    ask=re.search('ask',str(c))
    if ask:
        print "sorry no injection point found in this site"
    else:
        print c




   


    

if __name__=='__main__':
    Main()
