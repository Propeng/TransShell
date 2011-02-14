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

try:
  import pexpect
except ImportError:
  print "<> Unable to import pexpect. You are allowed to continue, but TransShell is likely to fail."

class Link():
  def __init__(self, conn, command, args):
    self.conn = conn
    self.command = command
    self.args = args

  def start(self):
    pass

  def stop(self):
    pass

  def stdout_read(self):
    pass

  def stderr_read(self):
    pass

  def stdin_write(self):
    pass
