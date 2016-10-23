#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

__copyright__ = """
    pyObjUtils - Object file library for Python.

   (C) 2010-2016 by Christoph Schueler <cpu12.gems@googlemail.com>

   All Rights Reserved

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from copy import copy
import io
import os
import unittest
from objutils import dump, dumps, load, loads, probe, probes


TEST2 = b''':100000004578616D706C65207769746820616E2039
:0B0010006164647265737320676170A7
:101000004865726520697320612067617020696E90
:1010100020746865206D656D6F727920616C6C6FEE
:06102000636174696F6E4C
:00000001FF
'''

TEST3 = b''':020000022BC011
:1012340054686973207061727420697320696E2028
:0D12440061206C6F77207365676D656E74B7
:020000027F007D
:1080000054686973207061727420697320696E20EE
:108010007468652068696768207365676D656E744C
:00000001FF
'''

TEST4 = b""":0D00000048656C6C6F2C20576F726C640AA1
:00000001FF"""


class TestIHex(unittest.TestCase):

    def testAddressGapFromString(self):
        data = loads("ihex", TEST2)
        self.assertEqual(data.sections[0].data, b'Example with an address gap')
        self.assertEqual(data.sections[1].data, b'Here is a gap in the memory allocation')

    def testAddressGapFromFileLike(self):
        data = load("ihex", io.BytesIO(TEST2))
        self.assertEqual(data.sections[0].data, b'Example with an address gap')
        self.assertEqual(data.sections[1].data, b'Here is a gap in the memory allocation')

    def testRoundtripFromString(self):
        dataIn = loads("ihex", TEST2)
        dataOut = dumps("ihex", dataIn)
        self.assertEqual(dataOut, TEST2)

    def testRoundtripFromFileLike(self):
        #pass
        dataIn = load("ihex", io.BytesIO(TEST2))
        dataOut = dumps("ihex", dataIn)
        self.assertEqual(dataOut, TEST2)

S19_16 = """S1130100000102030405060708090A0B0C0D0E0F73
S1130110101112131415161718191A1B1C1D1E1F63
S1130120202122232425262728292A2B2C2D2E2F53
S1130130303132333435363738393A3B3C3D3E3F43
S1130200000102030405060708090A0B0C0D0E0F72
S1130210101112131415161718191A1B1C1D1E1F62
S1130220202122232425262728292A2B2C2D2E2F52
S1130230303132333435363738393A3B3C3D3E3F42"""

S19_20 = """S214010000000102030405060708090A0B0C0D0E0F72
S214010010101112131415161718191A1B1C1D1E1F62
S214010020202122232425262728292A2B2C2D2E2F52
S214010030303132333435363738393A3B3C3D3E3F42
S214020000000102030405060708090A0B0C0D0E0F71
S214020010101112131415161718191A1B1C1D1E1F61
S214020020202122232425262728292A2B2C2D2E2F51
S214020030303132333435363738393A3B3C3D3E3F41"""

S19_32 = """S31500100000000102030405060708090A0B0C0D0E0F62
S31500100010101112131415161718191A1B1C1D1E1F52
S31500100020202122232425262728292A2B2C2D2E2F42
S31500100030303132333435363738393A3B3C3D3E3F32
S31500200000000102030405060708090A0B0C0D0E0F52
S31500200010101112131415161718191A1B1C1D1E1F42
S31500200020202122232425262728292A2B2C2D2E2F32
S31500200030303132333435363738393A3B3C3D3E3F22
"""

IHEX_16 =  b""":10010000000102030405060708090A0B0C0D0E0F77
:10011000101112131415161718191A1B1C1D1E1F67
:10012000202122232425262728292A2B2C2D2E2F57
:10013000303132333435363738393A3B3C3D3E3F47
:10020000000102030405060708090A0B0C0D0E0F76
:10021000101112131415161718191A1B1C1D1E1F66
:10022000202122232425262728292A2B2C2D2E2F56
:10023000303132333435363738393A3B3C3D3E3F46
:00000001FF
"""

IHEX_20 = b""":020000021000EC
:10000000000102030405060708090A0B0C0D0E0F78
:10001000101112131415161718191A1B1C1D1E1F68
:10002000202122232425262728292A2B2C2D2E2F58
:10003000303132333435363738393A3B3C3D3E3F48
:020000022000DC
:10000000000102030405060708090A0B0C0D0E0F78
:10001000101112131415161718191A1B1C1D1E1F68
:10002000202122232425262728292A2B2C2D2E2F58
:10003000303132333435363738393A3B3C3D3E3F48
:00000001FF
"""

IHEX_32 = b""":020000040010EA
:10000000000102030405060708090A0B0C0D0E0F78
:10001000101112131415161718191A1B1C1D1E1F68
:10002000202122232425262728292A2B2C2D2E2F58
:10003000303132333435363738393A3B3C3D3E3F48
:020000040020DA
:10000000000102030405060708090A0B0C0D0E0F78
:10001000101112131415161718191A1B1C1D1E1F68
:10002000202122232425262728292A2B2C2D2E2F58
:10003000303132333435363738393A3B3C3D3E3F48
:00000001FF
"""

class TestIHexRecordTypes(unittest.TestCase):

    def test16Bit(self):
        dataIn = loads("srec", S19_16)
        dataOut = dumps("ihex", dataIn)
        self.assertEqual(dataOut, IHEX_16)

    def test20Bit(self):
        dataIn = loads("srec", S19_20)
        dataOut = dumps("ihex", dataIn)
        self.assertEqual(dataOut, IHEX_20)

    def test32Bit(self):
        dataIn = loads("srec", S19_32)
        dataOut = dumps("ihex", dataIn)
        self.assertEqual(dataOut, IHEX_32)


def main():
    unittest.main()

if __name__=='__main__':
    main()

