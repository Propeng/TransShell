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
from link import Link
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
          if args[0] in self.links: #is channel already linked?
            print "<> %s already linked to %s, unlink first" % (self.links[args[0]].command, args[0])
          else:
            self.links[args[0]] = Link(args[1], args[2:])
            self.links[args[0]].start()
            conn.join(args[0])
            conn.privmsg(args[0], "[] Linking %s to %s" % (args[1], args[0]))
        elif command == "unlink":
          if args[0] in self.links:
            conn.privmsg(args[0], "[] Unlinking %s" % self.links[args[0]].command)
            self.links[args[0]].stop()
            del self.links[args[0]]
          else: #channel not linked
            print "<> %s is not linked to a program" % args[0]
        else:
          print "<> Unknown command: %s" % command
      else: #IRC command
        conn.send_raw(command)

  def welcome(self, conn, event):
    print "[] Connected, auto-joining %s" % Config.auto_join
    conn.join(Config.auto_join)
    print "[] Ready. Allowing channel commands %s and private messages %s" % (Config.allow_chan, Config.allow_priv)
    self.shell(conn)
