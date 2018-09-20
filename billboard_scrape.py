from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

years = ['1942', '1943', '1944', '2013']
data = []; data.append(['Year','Rating','Title','Artist'])
for year in years:
    content = urlopen('http://billboardtop100of.com/' + year + '-2/')
    c=content.read()
    soup = BeautifulSoup(c)
    ps = soup.find_all('p')
    if year == '1942':
        for p in ps:
            p = str(p)
            m = re.search('>(\d+)\.',p)
            try:
                rating = m.group(1)
            except:
                print(p)
            try:
                title = ''.join(p.split('<br')[0].split('.')[1:]).split(' by ')[0]
            except:
                print(p)
            try:
                artist = ''.join(p.split('<br')[0].split('.')[1:]).split(' by ')[1]
            except:
                print(p)
            data.append([year, rating, title, artist])
    elif year == '2013':
        for line in str(ps[2]).strip('<p>').strip('</p>').split('<br/>\n'):
            try:
                rating = line.split('.')[0]
                title = ''.join(line.split('.')[1:]).split(' – ')[0].rstrip()
                artist = ''.join(line.split('.')[1:]).split(' – ')[1]
                data.append([year, rating, title, artist])
            except:
                print(f'{year}\n{line}')
                break
    else:
        for line in str(ps[0]).strip('<p>').strip('</p>').split('<br/>\n'):
            try:
                rating = line.split('.')[0] 
                title = ''.join(line.split('.')[1:]).split(' – ')[0].rstrip()
                artist = ''.join(line.split('.')[1:]).split(' – ')[1]
                data.append([year, rating, title, artist])
            except:
                print(f'{year}\n{line}')
                break
        
#print('\n\n\n\n\n')
#print(data)
with open('data.csv','w+') as datafile:
    for line in data:
        line = str(line).strip('[').strip(']')+'\n'
        datafile.write(line)


# <p>1.Moonlight Cocktail by The Glenn Miller Orchestra<br/>
# written by Kim Gannon &amp; Lucky Roberts</p>
# <p>2.(I’ve Got a Gal In) Kalamazoo by The Glenn Miller Orchestra<br/>
# written by Mack Gordon &amp; Harry Warren</p>
# <p>3.There Are Such Things by Tommy Dorsey and His Orchestra<br/>
# vocals by Frank Sinatra &amp; The Pied Pipers<br/>
# written by Stanley Adams, Abel Baer &amp; George W. Meyer</p>