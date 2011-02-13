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

class Config:
  SERVER_NAME = "irc.foonet.com"
  SERVER_PORT = "6667"
  BOT_NICK    = "TransShell"
  BOT_USER    = "ts"
  BOT_REAL    = "TransShell"

  AUTO_JOIN   = "#channel1,#channel2"
  CHAN_PREFIX = ";"
  ALLOW_CHAN  = True
  ALLOW_PRIV  = True

  AUTH_TYPE   = 0 # 0 = no auth, 1 = AUTH_NICK, 2 = AUTH_PASS
  #AUTH_NICK   = "adminnick"
  #AUTH_PASS   = "secretpassword"
