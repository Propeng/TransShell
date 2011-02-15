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
  server_name = "irc.foonet.com"
  server_port = 6667
  server_pass = None
  bot_nick    = "TransShell"
  bot_user    = "ts"
  bot_real    = "TransShell"

  auto_join   = "#channel1,#channel2"
  chan_prefix = ";"
  allow_chan  = True
  allow_priv  = True

  auth_type   = 0 # 0 = no auth, 1 = auth_nick, 2 = auth_pass
  #auth_nick   = "adminnick"
  #auth_pass   = "secretpassword"

  custom_env  = {"PS1": "\\$"} # extra environment variables
