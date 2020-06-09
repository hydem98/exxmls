import re,urllib2

url = 'https://www.mmnt.net/db/0/0/89.178.212.206/Disk_H/torrents/xxx'
iconimage = ''
fanart = ''
name =''


def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != 'https://www.mmnt.net/db/0/0/89.178.212.206/Disk_H/torrents/xxx':
        return link
    else:
        link = 'Opened'
        return link

def Main_Loop(url,name,iconimage,fanart):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="(.+?)">(.+?)</a>').findall(HTML)
    for url2,name in match:
        url3 = url + url2
        if '..' in url3:
            pass
        elif 'rar' in url3:
            pass
        elif 'jpg' in url3:
            pass
        elif 'vtx' in url3:
            pass
        elif 'srt' in url3:
            pass
        elif 'C=' in url2:
            pass
        elif '/' in url2:
            Main_Loop(url3,name,iconimage,fanart)
            
        else:
            Clean_name(name,url3,iconimage,fanart)

def Clean_name(name,url3,iconimage,fanart):
    name1 = (name).replace('S01E','S01 E').replace('(MovIran).mkv','').replace('The.Walking.Dead','').replace('.mkv','').replace('Tehmovies.com.mkv','').replace('Nightsdl','').replace('Ganool','')
    name2=(name1).replace('.',' ').replace(' (ParsFilm).mkv','').replace('_TehMovies.Com.mkv','').replace(' (SaberFun.IR).mkv','').replace('[UpFilm].mkv','').replace('(Bia2Movies)','')
    name3=(name2).replace('.mkv','').replace('.Film2Movie_INFO.mkv','').replace('.HEVC.Film2Movie_INFO.mkv','').replace('.ParsFilm.mkv ','').replace('(SaberFunIR)','')
    name4=(name3).replace('.INTERNAL.','').replace('.Film2Movie_INFO.mkv','').replace('.web-dl.Tehmovies.net.mkv','').replace('S01E06','S01 E06').replace('S01E07','S01 E07')
    name5=(name4).replace('S01E08','S01 E08').replace('S01E09','S01 E09').replace('S01E10','S01 E10').replace('.Tehmovies.net','').replace('.WEBRip.Tehmovies.com.mkv','')
    name6=(name5).replace('.mp4','').replace('.mkv','').replace('.Tehmovies.ir','').replace('x265HEVC','').replace('Film2Movie_INFO','').replace('Tehmovies.com.mkv','')
    name7=(name6).replace(' (ParsFilm)','').replace('Tehmovies.ir.mkv','').replace('.480p',' 480p').replace('.WEBrip','').replace('.web-dl','').replace('.WEB-DL','')
    name8=(name7).replace('.','').replace('.Tehmovies.com','').replace('480p.Tehmovies.net</',' 480p').replace('720p.Tehmovies.net','720p').replace('.480p',' 480p')
    name9=(name8).replace('.480p.WEB-DL',' 480p').replace('.mkv','').replace('.INTERNAL.','').replace('720p',' 720p').replace('.Tehmovi..&gt;','').replace('.Tehmovies.net.mkv','')
    name10=(name9).replace('..720p',' 720p').replace('.REPACK.Tehmovies..&gt;','').replace('.Tehmovies.com.mkv','').replace('.Tehmovies..&gt;','').replace('Tehmovies.ir..&gt;','')
    name11=(name10).replace('Tehmovies.ne..&gt;','').replace('.HDTV.x264-mRs','').replace('...&gt;','').replace('.Tehmovies...&gt;','').replace('.Tehmovies.com.mp4','')
    name12=(name11).replace('.Tehmovies.com.mp4','').replace('_MovieFarsi','').replace('_MovieFar','').replace('_com','').replace('&gt;','').replace('avi','').replace('(1)','')
    name13=(name12).replace('(2)','').replace('cd 2','').replace('cd 1','').replace('-dos-xvid','').replace('divx','').replace('Xvid','').replace('DVD','').replace('DVDrip','')
    name14=(name13).replace('DvDrip-aXXo','').replace('[','').replace(']','').replace('XviD-TLF-','').replace('CD1','').replace('CD2','')
    name15=(name14).replace('Metallica','. ').replace('mp3','').replace('&amp;','&').replace('flac','').replace('-',' ').replace('  ',' ').replace('_',' ').replace('mp4','').replace('metallica','')
    clean_name = name15
    if iconimage == '':
        iconimage = ' '
    if fanart == '':
        fanart = ' '
    print '<item>'
    print '    <title>'+clean_name+'</title>'
    print '    <Link>'+url3+'</link>'
    print '    <thumbnail>'+iconimage+'</thumbnail>'
    print '</item>'
    print '\n'
    # edit above to suit your layout using the variables provided

Main_Loop(url,name,iconimage,fanart)

