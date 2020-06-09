import re, urllib2

def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


def web_scrape():
    HTML = OPEN_URL('http://dl3.film2movie.biz/serial/')
    regex = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(HTML)
    for url,name in regex:
        print '<plugin>' 
        print '<name>'+(name).replace("%20"," ").replace("&amp;","&").replace("/","")+'</name>'
        print '<link>http://dl3.film2movie.biz/serial/''+(name).replace("%20"," ").replace("&amp;","&")+''</link'
        print '<thumbnail>http://karnage.dark-avengers.com/images/icons/karicon.jpg</thumbnail>'
        print '</plugin>'
        print
        
def web_scrape2():
    HTML = OPEN_URL('https://nyaa.si/')
    regex = re.compile('<td><a href="(.+?)">(.+?)</td>').findall(HTML)
    for url,name in regex:
        print '<plugin>' 
        print '<name>'+(name).replace("%20"," ").replace("&amp;","&").replace("/","")+'</name>'
        print '<link>http://dl3.film2movie.biz/serial/''+(name).replace("%20"," ").replace("&amp;","&")+''</link'
        print '<thumbnail>http://karnage.dark-avengers.com/images/icons/karicon.jpg</thumbnail>'
        print '</plugin>'
        print

def web_scrape3():
    HTML = OPEN_URL('http://dl3.film2movie.biz/serial/')
    regex = re.compile('<pre><a href="(.+?)">(.+?)</pre>').findall(HTML)
    for url,name in regex:
        print '<plugin>' 
        print '<name>'+(name).replace("%20"," ").replace("&amp;","&").replace("/","")+'</name>'
        print '<link>http://dl3.film2movie.biz/serial/''+(name).replace("%20"," ").replace("&amp;","&")+''</link'
        print '<thumbnail>http://karnage.dark-avengers.com/images/icons/karicon.jpg</thumbnail>'
        print '</plugin>'
        print

#web_scrape()
web_scrape2()
#web_scrape3()


