# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PluginTemplate
                                 A QGIS plugin
 plugin_template
                              -------------------
        begin                : 2015-03-17
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Pirmin Kalberer
        email                : pka@sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from ..plugin_template import PluginTemplate


class ProcessingProviderPluginTemplate(PluginTemplate):

    def descr(self):
        return "Processing Provider"

    def subdir(self):
        return os.path.dirname(__file__)

    def template_map(self, specification, dialog):
        specification.category = 'Analysis'
        return {
            # Makefile
            'TemplatePyFiles': '',
            'TemplateUiFiles': '',
            'TemplateExtraFiles': '',
            'TemplateQrcFiles': '',
            'TemplateRcFiles': '',
        }

    def template_files(self, specification):
        return {
            'module_name_algorithm.tmpl':
            '%s_algorithm.py' % specification.module_name,
            'module_name_provider.tmpl':
            '%s_provider.py' % specification.module_name,
        }
