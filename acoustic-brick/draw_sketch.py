#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'E:/pvardanis/workshop/acoustic-brick')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

geomObj_1 = geompy.MakeVertex(0, 0, 0)
x = geompy.MakeVectorDXDYDZ(1, 0, 0)
y = geompy.MakeVectorDXDYDZ(0, 1, 0)
z = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_5 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(0.0000000, 1.0910000)
sk.addArcRadiusAbsolute(0.8660000, 1.9570000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(1.3990000, 1.9570000)
sk.addArcAbsolute(1.3990000, 2.3900000)
sk.addSegmentAbsolute(0.8660000, 2.3900000)
sk.addArcRadiusAbsolute(0.0000000, 3.2570000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(0.0000000, 3.9670000)
sk.addArcRadiusAbsolute(0.8660000, 4.8330000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(1.3990000, 4.8330000)
sk.addArcAbsolute(1.3990000, 5.2660000)
sk.addSegmentAbsolute(0.8660000, 5.2660000)
sk.addArcRadiusAbsolute(0.0000000, 6.1320000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(0.0000000, 8.6610000)
sk.addSegmentAbsolute(3.8480000, 8.6610000)
sk.addSegmentAbsolute(3.8480000, 7.5700000)
sk.addArcRadiusAbsolute(2.9810000, 6.7040000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(2.4480000, 6.7040000)
sk.addArcAbsolute(2.4480000, 6.2710000)
sk.addSegmentAbsolute(2.9810000, 6.2710000)
sk.addArcRadiusAbsolute(3.8480000, 5.4050000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(3.8480000, 4.6940000)
sk.addArcRadiusAbsolute(2.9810000, 3.8280000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(2.4480000, 3.8280000)
sk.addArcAbsolute(2.4480000, 3.3950000)
sk.addSegmentAbsolute(2.9810000, 3.3950000)
sk.addArcRadiusAbsolute(3.8480000, 2.5290000, -0.8660000, 0.0000000)
sk.addSegmentAbsolute(3.8480000, 0.0000000)
sk.addSegmentAbsolute(0.0000000, 0.0000000)
sk.addSegmentAbsolute(0.0000000, 1.0910000)
Sketch = sk.wire(geomObj_5)
geompy.addToStudy( x, 'x' )
geompy.addToStudy( y, 'y' )
geompy.addToStudy( z, 'z' )
geompy.addToStudy( Sketch, 'Sketch' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

try:
  pass
except:
  print('ExportUNV() failed. Invalid file name?')




if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
