# -*- coding: utf-8 -*-
"""
/***************************************************************************
 burgerVille
                                 A QGIS plugin
 make this work
                             -------------------
        begin                : 2014-02-23
        copyright            : (C) 2014 by Brylie and katie
        email                : this@that.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load burgerVille class from file burgerVille
    from burgerville import burgerVille
    return burgerVille(iface)
