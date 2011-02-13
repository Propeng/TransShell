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
  def main(self):
    # connect to network and join channels
    irc = irclib.IRC()
    server = irc.server()
    server.connect(Config.server_name, Config.server_port, Config.bot_nick, Config.server_pass, Config.bot_user, Config.bot_real)
    server.join(Config.auto_join)
    irc.process_forever()
