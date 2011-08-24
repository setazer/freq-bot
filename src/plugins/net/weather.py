#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Imported from talisman by quality(quality@botaq.net)
#Official conference - botaq@conference.jabber.ru
#Thanks to Gigabyte


import urllib
from xml.dom import minidom


def weather(t, s, p):
        if not p:
                s.msg(t, u'город?')
                return
        CITY = urllib.quote(p.encode('cp1251'))
        link = u'http://pda.rp5.ru/?lang=ru&q=%CITY%'.replace('%CITY%', CITY)
        try:
                r = urllib.urlopen(link)
                target = r.read()
                r.close()
        except:
                s.msg(t, u'не возможно установить соединение, попробуйте позже.')
                return
        if target.count('1. <a href="'):
                try:
                        od = re.search('1. <a href="',target)
                        b1 = target[od.end():]
                        b1 = b1[:re.search('">',b1).start()]
                        kod = b1
                except:
                        s.msg(t, u'неизвестная ошибка (ошибка парсинга страницы поиска)')
                        return
        else:
                s.msg(t, u'не найден населенный пункт')
                return

        try:
                r = urllib.urlopen('http://rp5.ru/rss/%KOD%'.replace('%KOD%', kod))
                dom = minidom.parse(r)
        except:
                s.msg(t, u'не возможно установить соединение, попробуйте позже.')
                return

        RES = ''
        ret = ''
        try:
                for x in dom.getElementsByTagName('item'):
                        mtiile = x.getElementsByTagName('title')[0].firstChild.data.strip().split(': ', 1)
                        ww = x.getElementsByTagName('description')[0].firstChild.data.strip()
                        ww = ww.replace(',', '\n')
                        ww = ww.replace('%)', '% )')
                        ret += '['+mtiile[1]+u']\nТемпература: %s\n' % ww
                        ret += u' - - - - - - - - - - \n'
                RES = u'Погода в городе '+mtiile[0]+'\n - - - - - - - - - - \n'+ret
                s.msg(t, RES)
        except:
                s.msg(t, u'неизвестная ошибка! скорее всего это косяк бета версии т.к. некоторые украинские города надо грузить с другого ресурса.')

				
bot.register_cmd_handler(weather, u'.weather')