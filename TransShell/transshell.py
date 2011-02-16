#!/usr/bin/python
# TransShell: An interactive shell-to-IRC bot.
# Copyright (C) 2011 Ahmed El-Mahdawy <aa.mahdawy.10@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, irclib, thread
import shell
from config import Config

class TransShell():
  def __init__(self):
    self.links = {}
    for envval in Config.custom_env:
      os.environ[envval] = Config.custom_env[envval]

  def main(self):
    print "[] Connecting to %s:%d" % (Config.server_name, Config.server_port)

    # connect to network
    irc = irclib.IRC()
    server = irc.server()
    server.connect(Config.server_name, Config.server_port, Config.bot_nick, Config.server_pass, Config.bot_user, Config.bot_real)

    # handlers
    irc.add_global_handler("welcome", self.welcome)
    irc.add_global_handler("privmsg", self.privmsg)
    irc.add_global_handler("pubmsg", self.pubmsg)
    irc.process_forever()

  def welcome(self, conn, event):
    print "[] Connected, auto-joining %s" % Config.auto_join
    conn.join(Config.auto_join)
    print "[] Ready. Allowing channel commands %s and private messages %s" % (Config.allow_chan, Config.allow_priv)
    thread.start_new_thread(shell.shell, (self.links, conn))

  def privmsg(self, conn, event):
    nick = event.source().split('!')[0]
    self.handlemsg(event.arguments()[0], nick, nick)

  def pubmsg(self, conn, event):
    message = event.arguments()[0]
    if message.startswith(Config.chan_prefix):
      nick = event.source().split('!')[0]
      self.handlemsg(message[len(Config.chan_prefix):], event.target(), nick)

  def handlemsg(self, message, linkto, nick):
    if linkto in self.links: #only respond if channel is linked to
      self.links[linkto].queue.append(message)
