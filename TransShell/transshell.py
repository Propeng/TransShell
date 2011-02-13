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

from config import Config
import irclib

class TransShell():
  def __init__(self):
    self.links = {}

  def main(self):
    print "[] Connecting to %s:%d" % (Config.server_name, Config.server_port)

    # connect to network
    irc = irclib.IRC()
    server = irc.server()
    server.connect(Config.server_name, Config.server_port, Config.bot_nick, Config.server_pass, Config.bot_user, Config.bot_real)

    # handlers
    irc.add_global_handler("welcome", self.welcome)
    irc.process_forever()

  def shell(self, conn):
    while True:
      # prompt for input
      command = raw_input("shell> ")
      if command.startswith(";"): #internal command
        # split to command and args
        internal = command[1:]
        split = internal.split(' ')
        args = split[1:]
        command = split[0]

        # run command
        if command == "link":
          pass
        elif command == "unlink":
          pass
        else:
          print "<> Unkown command: %s" % command
      else: #IRC command
        conn.send_raw(command)

  def welcome(self, conn, event):
    print "[] Connected, auto-joining %s" % Config.auto_join
    conn.join(Config.auto_join)
    print "[] Ready. Allowing channel commands %s and private messages %s" % (Config.allow_chan, Config.allow_priv)
    self.shell(conn)
