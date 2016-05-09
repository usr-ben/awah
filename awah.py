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
    import urllib,urllib2
    from bs4 import BeautifulSoup
    import re

    url=url.replace("www.","")
    dork="inurl:php?id= site:"+url
    
    encode=urllib.quote(dork)
    url="http://uk.ask.com/web?q="+ encode

    raw = urllib2.urlopen(url).read()
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
        site= c+"'"
        a=urllib2.urlopen(site).read()
        errors = ["You have an error in your SQL syntax","Execution of a query to the database failed", "Unknown column", "404 Error Message", "mysql_num_rows()",
               "mysql_fetch_array()", "Error Occurred While Processing Request","Server Error in '/' Application",
               "Microsoft OLE DB Provider for ODBC Drivers error", "error in your SQL syntax", "include()",
               "Invalid Querystring", "OLE DB Provider for ODBC","Error: You have an error in your SQL syntax", "VBScript Runtime", "ADODB.Field", "BOF or EOF",
               "ADODB.Command","JET Database","mysql_fetch_row()", "Syntax error", "mysql_fetch_assoc()", "mysql_fetch_object()",
               "mysql_numrows()", "GetArray()", "FetchRow()","input string was not in a correct format",
               "MSSQL_Uqm: Unclosed quotation mark","JDBC_CFM2 : SQLServer JDBC Driver", "JDBC_CFM': Error Executing Database Query", "Oracle: ORA-01756","Division by zero",
               "Failed Query"]
        d=len(errors)
        if a:
            for i in range(d):
                c=errors[i]
                b=re.search(c,a)
                if b:
                    break

            print "site is vulnerable"
    
        else:
            print "site is not vulnerable"

if __name__=='__main__':
    Main()
