# (C) 2015 see Authors.txt
#
# This file is part of MPC-HC.
#
# MPC-HC is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# MPC-HC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import fnmatch

from UpdatePOT import *
from UpdatePO import *
from UpdateRC import *

if __name__ == '__main__':
    print 'Updating POT file'
    UpdatePOT()
    print '----------------------'

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.rc'):
            print file
            file = os.path.splitext(file)[0]
            print '--> Updating PO files'
            UpdatePO(file)
            print '--> Updating RC file'
            UpdateRC(file, False)
            print '----------------------'
