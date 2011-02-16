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

import sys, os, signal, itertools
from threading import Timer
from repeattimer import RepeatTimer
try:
  import pty
except ImportreadError:
  print "<> ImportreadError: pty module was not found, exiting"
  sys.exit(1)

class Link():
  def __init__(self, conn, chan, command, args):
    self.conn = conn
    self.chan = chan
    self.command = command
    self.args = args
    self.queue = []

  def start(self):
    self.pid, self.child = pty.fork()
    if self.pid == 0: #is child process?
      finalargs = self.args
      if self.args == []:
        finalargs = [""]
      os.execv(self.command, finalargs)
    else:
      self.intimer = RepeatTimer(1, self.syncin)
      self.outtimer = Timer(1, self.syncout)
      self.intimer.start()
      self.outtimer.start()

  def stop(self):
    self.intimer.cancel()
    self.outtimer.cancel()
    os.kill(self.pid, signal.SIGKILL)

  def syncin(self):
    if self.queue != []:
      for line in self.queue:
        os.write(self.child, line + "\r\n")
      self.queue = []

  def syncout(self):
    try:
      readstr = os.read(self.child, 1024)
      lines = itertools.groupby(readstr.splitlines())
      for line in lines:
        if line[0] != "":
          self.conn.privmsg(self.chan, "[%s] %s" % (self.command, line[0]))
      self.outtimer = Timer(2, self.syncout)
      self.outtimer.start()
    except OSError:
      self.conn.privmsg(self.chan, "[] %s terminated" % self.command)
