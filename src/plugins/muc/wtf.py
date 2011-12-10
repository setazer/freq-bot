#!/usr/bin/env python
# -*- coding: utf8 -*-
#~#######################################################################
#~ Copyright (c) 2008 Burdakov Daniel <kreved@kreved.org>               #
#~ Copyright (c) 2010 Kazakov Alexandr <ferym@jabber.ru>                #
#~ Copyright (c) 2011 Timur Timirkkhanov <tlemur@jabber.ru>             #
#~                                                                      #
#~ This file is part of FreQ-bot.                                       #
#~                                                                      #
#~ FreQ-bot is free software: you can redistribute it and/or modify     #
#~ it under the terms of the GNU General Public License as published by #
#~ the Free Software Foundation, either version 3 of the License, or    #
#~ (at your option) any later version.                                  #
#~                                                                      #
#~ FreQ-bot is distributed in the hope that it will be useful,          #
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
#~ GNU General Public License for more details.                         #
#~                                                                      #
#~ You should have received a copy of the GNU General Public License    #
#~ along with FreQ-bot.  If not, see <http://www.gnu.org/licenses/>.    #
#~#######################################################################

import db

def dfn_handler(t, s, p):
  p = p.strip()
  if p:
   wtf_db = db.database('wtf')
   kv = p.split('=', 1)
   if not len(kv)<2:
    key = kv[0].lower().strip()
    val = kv[1].strip()
    if not val:
     try:
      wtf_db.query('delete from wtf where room=? and key=?',(s.room.jid,key))
      wtf_db.commit()
      s.lmsg(t,'dfn_remove')
     except: s.lmsg(t,'dfn_failed')
    else:
     wtf_db.query('delete from wtf where room=? and key=?',(s.room.jid,key))
     wtf_db.query('insert into wtf values (?,?,?)',(s.room.jid,key,val+"\n(by %s %s)" % (s.nick,time.strftime("%d.%m.%Y %H:%M:%S"))))
     wtf_db.commit()
     s.lmsg(t,'dfn_save')
   else: s.lmsg(t,'dfn_empty')
  else: s.lmsg(t,'dfn_empty')

def wtf_handler(t,s,p):
 p=p.strip()
 if not p: s.lmsg(t,'wtf_empty'); return
 wtf_db = db.database('wtf')
 try:
  res = wtf_db.query('select val from wtf where room=? and key=?',(s.room.jid,params)).fetchone()
  s.lmsg(t,'wtf_result',p,''.join(res))
  cn.close()
 except: s.lmsg(t,'wtf_not_found'); cn.close()
 
def wtfnames_handler(t,s,params):
 wtf_db = db.database('wtf')
 keys = wtf_db.query('select * from wtf where room=?',(s.room.jid,))
 res = []
 try:
  for i in keys:
   res.append(i[1])
  if len(res)==0: s.lmsg(t,'wtfnames_empty'); return
  s.lmsg(t,'wtfnames_result',', '.join(res),str(len(res)))
 except: s.lmsg(t,'failed')
 
def wtfsearch_handler(t,s,params):
 if not params: s.lmsg(t,'wtfsearch_not_parameters'); return
 wtf_db = db.database('wtf')
 params = '%'+params+'%'
 try:
  res = wtf_db.query('select * from wtf where (room=?) and (key like ? or val like ?)',(s.room.jid,params,params))
  out = []
  for i in res:
   out.append(i[1])
  if len(out)<1: s.lmsg(t,'wtfsearch_error'); return
  s.lmsg(t,'wtfsearch_result',', '.join(out))
 except: s.lmsg(t,'wtfsearch_error')

bot.register_cmd_handler(dfn_handler, '.dfn', 9)
bot.register_cmd_handler(wtf_handler, '.wtf')
bot.register_cmd_handler(wtfnames_handler, '.wtfnames')
bot.register_cmd_handler(wtfsearch_handler, '.wtfsearch')
