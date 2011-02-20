#!/usr/bin/env python
# -*- coding: utf-8 -*-

import HexFile

DATA=1
EOF=2

FORMATS=(
    (DATA,"/AAAALLBBDDCC"),
    (EOF,"/AAAA00BB"),
)

class Reader(HexFile.Reader):
    def __init__(self,inFile):
        super(Reader,self).__init__(FORMATS,inFile)

    def nibbleSum(self,accu,b):
        hn=(b & 0xf0) >> 4
        ln=b & 0x0f
        s=hn+ln
        return accu+s

    def checkLine(self,line,formatType):
        if formatType==DATA:
            if line.length!=len(line.chunk):
                raise HexFile.InvalidRecordLengthError("Byte count doesn't match length of actual data.")
            addrChecksum=0
            for b in [(line.address & 0xff00)>>8,line.address & 0xff,line.length]:
                addrChecksum=self.nibbleSum(addrChecksum,b)
            if line.addrChecksum!=addrChecksum:
                raise HexFile.InvalidRecordChecksumError()
            checksum=0
            for b in line.chunk:
                checksum=self.nibbleSum(checksum,b)
            if line.checksum!=checksum:
                raise HexFile.InvalidRecordChecksumError()

    def isDataLine(self,line,formatType):
        return formatType==DATA

