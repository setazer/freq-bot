#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Imported from isida, talisman by quality(quality@botaq.net)
#Official conference - botaq@conference.jabber.ru
#Thanks to Disabler, Avinar, Als, Gigabyte, dr.Schmurge, PoisoneD, ferym

import urllib2,re,urllib
from re import compile as re_compile
strip_tags = re_compile(r'<[^<>]+>')


def ukrbashorg(t, s, p):
    if p.strip()=='':
        req = urllib2.Request('http://ukrbash.org/random')
    else:
        req = urllib2.Request('http://ukrbash.org/quote/'+p.strip())
    req.add_header = ('User-agent', 'Mozilla/5.0')
    try:
	r = urllib2.urlopen(req)
	target = r.read()
	od = re.search('</div><div>',target)
	message = target[od.end():]
	message = message[:re.search('</div></div></div>',message).start()]
	message = decode(message)
	message = '\n' + message.strip()
	s.msg(t,unicode(message,'utf-8'))
    except:
        s.msg(t,unicode('кінчився інтернет, все, приїхали...','utf8'))
		
		
bot.register_cmd_handler(ukrbashorg, u'.ukrbor') 		


def ostrie(t, s, p):
    if p.strip()=='':
        req = urllib2.Request('http://ostrie.moskva.com/?do=TopToday')
    else:
        req = urllib2.Request('http://ostrie.moskva.com/?do=Item&id='+p.strip())
        req.add_header = ('User-agent', 'Mozilla/5.0')
    try:
        r = urllib2.urlopen(req)
        target = r.read()
        od = re.search('<dd>',target)
        message = target[od.end():]
        message = message[:re.search('<div class="instr">',message).start()]
        message = decode(message)
        message = '\n' + message.strip()
        s.msg(t,unicode(message,'koi8-r'))
    except:
        s.msg(t,unicode('Кончился интернет, всё, приехали...','utf8'))
		
		
bot.register_cmd_handler(ostrie, u'.ostrie')     
        
		
def bashorgru_abyss(t, s, p):
    if p.strip()=='':
        req = urllib2.Request('http://bash.org.ru/abysstop')
    else:
        s.msg(t,u'бездна не поддерживает номера')
        return
    req.add_header = ('User-agent', 'Mozilla/5.0')
    try:
        r = urllib2.urlopen(req)
        target = r.read()
        id=str(random.randrange(1, 25))
        od = re.search('<b>'+id+':',target)
        q1 = target[od.end():]
        q1 = q1[:re.search('\n</div>',q1).start()]
        od = re.search('<div>',q1)
        message = q1[od.end():]
        message = message[:re.search('</div>',message).start()]	         
        message = decode(message)
        message = '\n' + message.strip()
        s.msg(t,unicode(message,'windows-1251'))
    except:
        s.msg(t,u'аблом какой-то')
		
		
bot.register_cmd_handler(bashorgru_abyss, u'.borb')


def nya(t, s, p):
    if p.strip()=='':
        req = urllib2.Request('http://nya.sh/')
    else:
        s.msg(t,u'в разработке')
        return
    req.add_header = ('User-agent', 'Mozilla/5.0')

    try:
        r = urllib2.urlopen(req)
        target = r.read()

	od = re.search('<div align="right" class="sm"><a href="/', target)
	b1 = target[od.end():]
	b1 = b1[:re.search('"><b>',b1).start()]

	posts = b1.split('/')
	post = random.randrange(1, int(posts[1]))
	adres = 'http://nya.sh/post/'+str(post)
	req = urllib2.Request(adres)

	r = urllib2.urlopen(req)
	target = r.read()


	od = re.search('</i></div><br />', target)
	b1 = target[od.end():]
	b1 = b1[:re.search('</div>',b1).start()]
	b1 = decode(b1)

        message = b1
        s.msg(t, u'цитата #'+str(post)+u':\n'+unicode(message,'windows-1251'))
    except:
        s.msg(t,u'повторите запрос')

		
bot.register_cmd_handler(nya, u'.nya')


def ithappens(t, s, p):
    if p.strip()=='':
        req = urllib2.Request('http://ithappens.ru/')
    else:
        s.msg(t,u'в разработке')
        return
    req.add_header = ('User-agent', 'Mozilla/5.0')

    try:
        r = urllib2.urlopen(req)
        target = r.read()

	od = re.search('<h3><a href="/', target)
	b1 = target[od.end():]
	b1 = b1[:re.search('">',b1).start()]

	posts = b1.split('/')
	post = random.randrange(1, int(posts[1]))
	adres = 'http://ithappens.ru/story/'+str(post)
	req = urllib2.Request(adres)

	r = urllib2.urlopen(req)
	target = r.read()


	od = re.search('<p class="text">', target)
	b1 = target[od.end():]
	b1 = b1[:re.search('</p>',b1).start()]
	b1 = decode(b1)

        message = b1
        s.msg(t, u'цитата #'+str(post)+u':\n'+unicode(message,'windows-1251'))
    except:
        s.msg(t,u'повторите запрос')

		
bot.register_cmd_handler(ithappens, u'.it')


def sonnik(t, s, p):
        if not p:
                s.msg(t, u'введи слово')
                return

        req = urllib2.Request('http://sonnik.ru/search.php?key='+p.encode('windows-1251'))
        req.add_header = ('User-agent', 'Mozilla/5.0')
        r = urllib2.urlopen(req)
        target = r.read()

        try:
        	od2 = re.search('</p><br><p class="smalltxt"><strong>', target)
	        data2 = target[od2.end():]
	        data2 = data2[:re.search('<br><strong>', data2).start()]

        	od21 = re.search('html">', data2)
	        data21 = data2[od21.end():]
	        data21 = data21[:re.search('</a>', data21).start()]
        except:
                data21 = '-'

        try:
        	od1 = re.search('<title>', target)
	        data1 = target[od1.end():]
	        data1 = data1[:re.search("</title>", data1).start()]
	
	        od = re.search('<p id="main3">', target)
	        data = target[od.end():]
	        data = data[:re.search("</p>", data).start()]
	        data = decode(data)
        except:
                s.msg(t, u'ошибка')
                return

	s.msg(t, u'тема: '+unicode(data21, "windows-1251").strip()+'\n'+unicode(data1, "windows-1251").strip()+'\n'+unicode(data, "windows-1251").strip())

	
bot.register_cmd_handler(sonnik, u'.sonnik')


def anek(t, s, p):
 text = urllib.urlopen('http://www.anekdot.ru/scripts/rand_anekdot.php?').read()
 text = text[re.search('<pre>', text).end():]
 text = text[:re.search('</pre>', text).start()]
 s.msg(t, unicode(text, 'windows-1251'))

 
bot.register_cmd_handler(anek, u'.anek')


def afor(t, s, p):
    try:
        req = urllib2.Request('http://skio.ru/quotes/humour_quotes.php')
        req.add_header = ('User-agent', 'Mozilla/5.0')
        r = urllib2.urlopen(req)
        target = r.read()
        od = re.search('<form id="qForm" method="post"><div align="center">',target)
        message = target[od.end():]
        message = message[:re.search('</div>',message).start()]
        message = '\n' + message.strip()
        message = decode(message)
        s.msg(t, unicode(message,'windows-1251'))
    except:
        s.msg(t, u'что-то сломалось о_О')

		
bot.register_cmd_handler(afor, u'.afor')


def bash_org_ru(t, s, text):
	try: url, splitter = u'http://bash.org.ru/quote/'+str(int(text)), '<div class="q">'
	except: url, splitter = u'http://bash.org.ru/random', '<hr class="iq">'
	body = html_encode(urllib.urlopen(url).read())
	if body.count('<div class="vote">') > 1 and url.count('quote'): msg = u'цитата не найдена!'
	else:
		body = body.split('<div class="vote">')[1].split(splitter)[0]
		msg = u'http://bash.org.ru/quote/'+str(get_tag(body, 'a'))+u' '+rss_del_nn(rss_replace(body[body.find('[:||||:]'):].replace('</div>', '\n').replace('<div>', '').replace('[:||||:]', '::: ').replace('</a>\n', '')))
	s.msg(t, msg)

	
bot.register_cmd_handler(bash_org_ru, u'.bash')

	
def ibash_org_ru(t, s, text):
	try: url = u'http://ibash.org.ru/quote.php?id='+str(int(text))
	except: url = u'http://ibash.org.ru/random.php'
	body = html_encode(urllib.urlopen(url).read())
	msg = u'http://ibash.org.ru/quote.php?id='+replacer(body.split('<div class="quothead"><span>')[1].split('</a></span>')[0])[1:]
	if msg[-3:] == '???': msg = u'Цитата не найдена!'
	else: msg += '\n'+rss_replace(body.split('<div class="quotbody">')[1].split('</div>')[0])
	s.msg(t, msg)

	
bot.register_cmd_handler(ibash_org_ru, u'.ibash')


def decode(text):
    return strip_tags.sub('', text.replace('<br />','\n').replace('<br>','\n')).replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('\t','').replace('||||:]','').replace('>[:\n','').replace('&deg;', '°')
