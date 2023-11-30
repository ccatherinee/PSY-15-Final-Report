from bs4 import BeautifulSoup as soup
import os

#all_links is a file downloaded manually from the qreport website, there is one per semester
HTML = open("all_links", 'r')
html = HTML.read()
s = soup(html, 'lxml')
divs = s.find_all("div", {"class":"mb-2"})[1:]
links = [div.find("a")['href'] for div in divs]

for idx,link in enumerate(links):
    os.system("curl '"+link+"' --compressed -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://qreports.fas.harvard.edu/' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: CookieName="+COOKIE_NAME+"; cookiesession1="+COOKIE_SESSION+"; ASP.NET_SessionId="+SESSION_ID+"' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: cross-site' > "+str(idx))


directories = ['f19','f20','f21','f22','s21','s22','s23']
data = []
for directory in directories:
    for fn in os.listdir(directory)[1:]:
        try:
            #print(directory, fn)
            course_eval = soup(open(os.path.join(directory, fn),'r').read(), 'lxml')
            #looks like overall mean is always in the same place
            overall_mean = float(course_eval.find_all("tr", {"class":"CondensedTabularOddRows"})[1].find_all("td")[-2].contents[0])
            
            sections = course_eval.find("div",{"class":"ChildReportSkipNav"}).contents[0].find_all("li")
            num_sections = len(sections)
            
            if sections[6].contents[0].contents[0][:35] == 'On average, how many hours per week': #I think this is the typical case
                hours_mean = float(course_eval.find_all("tbody")[3].find_all("td")[2].contents[0])
            elif sections[4].contents[0].contents[0][:35] == 'On average, how many hours per week': #I think this is missing the two sections, "Instructor feedback for ...", "General Instructor Questions"
                hours_mean = float(course_eval.find_all("tbody")[2].find_all("td")[2].contents[0])
            data.append((overall_mean, hours_mean))
        except IndexError:
            print(directory, fn)
            print(os.path.getsize(os.path.join(directory,fn)))
            #almost always means that there were no responses, or one of the fields had no responses
        except:
            print(directory, fn)
            print("Unknown error")
import pickle
with open("data",'wb') as fp:
    pickle.dump(data, fp)
