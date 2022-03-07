# -*- coding: utf-8 -*-
"""
/***************************************************************************
 UFCAIDFDialog
                                 A QGIS plugin
 Lê dados de chuva para gerar equação IDF
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-05-18
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Laboratório de Recursos Hídricos (LAHI) - UFCA
        email                : jonas.nunes@aluno.ufca.edu.br
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

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# Isso carrega o arquivo .ui para que o PyQt possa preencher o plug-in com os elementos do Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'dialog\dialog_kolmogorov_smirnov.ui'))


class dialogKolmogorovSmirnov(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(dialogKolmogorovSmirnov, self).__init__(parent)
        self.setupUi(self)
        self.tableEstatisticaKS.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableEstatisticaKS.resizeColumnsToContents()