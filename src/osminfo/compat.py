# -*- coding: utf-8 -*-
# ******************************************************************************
#
# OSMInfo
# ---------------------------------------------------------
# This plugin takes coordinates of a mouse click and gets information about all
# objects from this point from OSM using Overpass API.
#
# Author:   Maxim Dubinin, sim@gis-lab.info
#           Denis Ilyin, denis.ilyin@nextgis.com
# *****************************************************************************
# Copyright (c) 2015-2021. NextGIS, info@nextgis.com
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
# ******************************************************************************

import os
import sys

from qgis import core

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


def get_file_dir(filename):
    return os.path.dirname(filename)


from qgis.core import Qgis as QGis


addMapLayer = core.QgsProject.instance().addMapLayer

PointGeometry = core.QgsWkbTypes.PointGeometry
PolygonGeometry = core.QgsWkbTypes.PolygonGeometry
LineGeometry = core.QgsWkbTypes.LineGeometry


class QgsCoordinateTransform(core.QgsCoordinateTransform):
    def __init__(self, src_crs, dst_crs):
        super(QgsCoordinateTransform, self).__init__()

        self.setSourceCrs(src_crs)
        self.setDestinationCrs(dst_crs)

    def setDestinationCrs(self, dst_crs):
        if QGis.QGIS_VERSION_INT >= 30000:
            super(QgsCoordinateTransform, self).setDestinationCrs(dst_crs)
        else:
            self.setDestCRS(dst_crs)


class QgsCoordinateReferenceSystem(core.QgsCoordinateReferenceSystem):
    def __init__(self, id, type):
        if QGis.QGIS_VERSION_INT >= 30000:
            super(QgsCoordinateReferenceSystem, self).__init__(
                core.QgsCoordinateReferenceSystem.fromEpsgId(id)
            )
        else:
            super(QgsCoordinateReferenceSystem, self).__init__(id, type)

    @staticmethod
    def fromEpsgId(id):
        if QGis.QGIS_VERSION_INT >= 30000:
            return core.QgsCoordinateReferenceSystem.fromEpsgId(id)
        else:
            return core.QgsCoordinateReferenceSystem(id)
