import urllib2
from BeautifulSoup import BeautifulSoup

x=1
s = raw_input("Enter a digit: ")
print "Started . . . "

while(x<=s):
    print BeautifulSoup(urllib2.urlopen("https://www.twitter.com/"+str(x))).title.string
    x+=1
    
