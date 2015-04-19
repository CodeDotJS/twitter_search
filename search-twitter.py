

import urllib2
from BeautifulSoup import BeautifulSoup

x=1

while(x<=n)
    print BeautifulSoup(urllib2.urlopen("https://www.twitter.com/"+str(x))).title.string
    x+=1
    


