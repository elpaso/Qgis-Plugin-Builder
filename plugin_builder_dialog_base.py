# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_builder_dialog_base.ui'
#
# Created: Thu Apr 17 23:54:57 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PluginBuilderDialogBase(object):
    def setupUi(self, PluginBuilderDialogBase):
        PluginBuilderDialogBase.setObjectName(_fromUtf8("PluginBuilderDialogBase"))
        PluginBuilderDialogBase.resize(554, 435)
        PluginBuilderDialogBase.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(PluginBuilderDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_box = QtGui.QDialogButtonBox(PluginBuilderDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(PluginBuilderDialogBase)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 523, 584))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.title_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.gridLayout_2.addWidget(self.title_label, 0, 0, 1, 2)
        self.class_name_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.class_name_label.setMinimumSize(QtCore.QSize(150, 0))
        self.class_name_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.class_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.class_name_label.setObjectName(_fromUtf8("class_name_label"))
        self.gridLayout_2.addWidget(self.class_name_label, 1, 0, 1, 1)
        self.class_name = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.class_name.setMinimumSize(QtCore.QSize(300, 0))
        self.class_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.class_name.setText(_fromUtf8(""))
        self.class_name.setObjectName(_fromUtf8("class_name"))
        self.gridLayout_2.addWidget(self.class_name, 1, 1, 1, 1)
        self.plugin_name_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plugin_name_label.setMinimumSize(QtCore.QSize(150, 0))
        self.plugin_name_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.plugin_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.plugin_name_label.setObjectName(_fromUtf8("plugin_name_label"))
        self.gridLayout_2.addWidget(self.plugin_name_label, 2, 0, 1, 1)
        self.title = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.title.setMinimumSize(QtCore.QSize(300, 0))
        self.title.setMaximumSize(QtCore.QSize(300, 16777215))
        self.title.setText(_fromUtf8(""))
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout_2.addWidget(self.title, 2, 1, 1, 1)
        self.description_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.description_label.setMinimumSize(QtCore.QSize(150, 0))
        self.description_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.description_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.description_label.setObjectName(_fromUtf8("description_label"))
        self.gridLayout_2.addWidget(self.description_label, 3, 0, 1, 1)
        self.description = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.description.setMinimumSize(QtCore.QSize(300, 0))
        self.description.setMaximumSize(QtCore.QSize(300, 16777215))
        self.description.setText(_fromUtf8(""))
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout_2.addWidget(self.description, 3, 1, 1, 1)
        self.module_name_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.module_name_label.setMinimumSize(QtCore.QSize(150, 0))
        self.module_name_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.module_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.module_name_label.setObjectName(_fromUtf8("module_name_label"))
        self.gridLayout_2.addWidget(self.module_name_label, 4, 0, 1, 1)
        self.module_name = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.module_name.setMinimumSize(QtCore.QSize(300, 0))
        self.module_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.module_name.setText(_fromUtf8(""))
        self.module_name.setObjectName(_fromUtf8("module_name"))
        self.gridLayout_2.addWidget(self.module_name, 4, 1, 1, 1)
        self.plugin_version_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plugin_version_label.setMinimumSize(QtCore.QSize(150, 0))
        self.plugin_version_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.plugin_version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.plugin_version_label.setObjectName(_fromUtf8("plugin_version_label"))
        self.gridLayout_2.addWidget(self.plugin_version_label, 5, 0, 1, 1)
        self.plugin_version = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.plugin_version.setMinimumSize(QtCore.QSize(60, 0))
        self.plugin_version.setMaximumSize(QtCore.QSize(60, 16777215))
        self.plugin_version.setObjectName(_fromUtf8("plugin_version"))
        self.gridLayout_2.addWidget(self.plugin_version, 5, 1, 1, 1)
        self.qgis_minimum_version_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.qgis_minimum_version_label.setMinimumSize(QtCore.QSize(150, 0))
        self.qgis_minimum_version_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.qgis_minimum_version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qgis_minimum_version_label.setObjectName(_fromUtf8("qgis_minimum_version_label"))
        self.gridLayout_2.addWidget(self.qgis_minimum_version_label, 6, 0, 1, 1)
        self.qgis_minimum_version = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.qgis_minimum_version.setMinimumSize(QtCore.QSize(60, 0))
        self.qgis_minimum_version.setMaximumSize(QtCore.QSize(60, 16777215))
        self.qgis_minimum_version.setObjectName(_fromUtf8("qgis_minimum_version"))
        self.gridLayout_2.addWidget(self.qgis_minimum_version, 6, 1, 1, 1)
        self.menu_text_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.menu_text_label.setMinimumSize(QtCore.QSize(150, 0))
        self.menu_text_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.menu_text_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.menu_text_label.setObjectName(_fromUtf8("menu_text_label"))
        self.gridLayout_2.addWidget(self.menu_text_label, 7, 0, 1, 1)
        self.menu_text = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.menu_text.setMinimumSize(QtCore.QSize(300, 0))
        self.menu_text.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menu_text.setText(_fromUtf8(""))
        self.menu_text.setObjectName(_fromUtf8("menu_text"))
        self.gridLayout_2.addWidget(self.menu_text, 7, 1, 1, 1)
        self.author_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.author_label.setMinimumSize(QtCore.QSize(150, 0))
        self.author_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.author_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.author_label.setObjectName(_fromUtf8("author_label"))
        self.gridLayout_2.addWidget(self.author_label, 8, 0, 1, 1)
        self.author = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.author.setMinimumSize(QtCore.QSize(300, 0))
        self.author.setMaximumSize(QtCore.QSize(300, 16777215))
        self.author.setText(_fromUtf8(""))
        self.author.setObjectName(_fromUtf8("author"))
        self.gridLayout_2.addWidget(self.author, 8, 1, 1, 1)
        self.email_address_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.email_address_label.setMinimumSize(QtCore.QSize(150, 0))
        self.email_address_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.email_address_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email_address_label.setObjectName(_fromUtf8("email_address_label"))
        self.gridLayout_2.addWidget(self.email_address_label, 9, 0, 1, 1)
        self.email_address = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.email_address.setMinimumSize(QtCore.QSize(300, 0))
        self.email_address.setMaximumSize(QtCore.QSize(300, 16777215))
        self.email_address.setText(_fromUtf8(""))
        self.email_address.setObjectName(_fromUtf8("email_address"))
        self.gridLayout_2.addWidget(self.email_address, 9, 1, 1, 1)
        self.optional_items_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.optional_items_label.setFont(font)
        self.optional_items_label.setAlignment(QtCore.Qt.AlignCenter)
        self.optional_items_label.setObjectName(_fromUtf8("optional_items_label"))
        self.gridLayout_2.addWidget(self.optional_items_label, 10, 0, 1, 1)
        self.tracker_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.tracker_label.setMinimumSize(QtCore.QSize(150, 0))
        self.tracker_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tracker_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tracker_label.setObjectName(_fromUtf8("tracker_label"))
        self.gridLayout_2.addWidget(self.tracker_label, 11, 0, 1, 1)
        self.tracker = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.tracker.setMinimumSize(QtCore.QSize(300, 0))
        self.tracker.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tracker.setObjectName(_fromUtf8("tracker"))
        self.gridLayout_2.addWidget(self.tracker, 11, 1, 1, 1)
        self.homepage_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.homepage_label.setMinimumSize(QtCore.QSize(150, 0))
        self.homepage_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.homepage_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.homepage_label.setObjectName(_fromUtf8("homepage_label"))
        self.gridLayout_2.addWidget(self.homepage_label, 12, 0, 1, 1)
        self.homepage = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.homepage.setMinimumSize(QtCore.QSize(300, 0))
        self.homepage.setMaximumSize(QtCore.QSize(300, 16777215))
        self.homepage.setObjectName(_fromUtf8("homepage"))
        self.gridLayout_2.addWidget(self.homepage, 12, 1, 1, 1)
        self.repository_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.repository_label.setMinimumSize(QtCore.QSize(150, 0))
        self.repository_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.repository_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repository_label.setObjectName(_fromUtf8("repository_label"))
        self.gridLayout_2.addWidget(self.repository_label, 13, 0, 1, 1)
        self.repository = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.repository.setMinimumSize(QtCore.QSize(300, 0))
        self.repository.setMaximumSize(QtCore.QSize(300, 16777215))
        self.repository.setObjectName(_fromUtf8("repository"))
        self.gridLayout_2.addWidget(self.repository, 13, 1, 1, 1)
        self.tags_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.tags_label.setMinimumSize(QtCore.QSize(150, 0))
        self.tags_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tags_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tags_label.setObjectName(_fromUtf8("tags_label"))
        self.gridLayout_2.addWidget(self.tags_label, 14, 0, 1, 1)
        self.tags = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.tags.setMinimumSize(QtCore.QSize(300, 0))
        self.tags.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tags.setObjectName(_fromUtf8("tags"))
        self.gridLayout_2.addWidget(self.tags, 14, 1, 1, 1)
        self.experimental = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.experimental.setObjectName(_fromUtf8("experimental"))
        self.gridLayout_2.addWidget(self.experimental, 15, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.class_name_label.setBuddy(self.class_name)
        self.plugin_name_label.setBuddy(self.title)
        self.description_label.setBuddy(self.description)
        self.module_name_label.setBuddy(self.module_name)
        self.plugin_version_label.setBuddy(self.plugin_version)
        self.qgis_minimum_version_label.setBuddy(self.qgis_minimum_version)
        self.menu_text_label.setBuddy(self.menu_text)
        self.author_label.setBuddy(self.author)
        self.email_address_label.setBuddy(self.email_address)
        self.tracker_label.setBuddy(self.tracker)
        self.homepage_label.setBuddy(self.homepage)
        self.repository_label.setBuddy(self.repository)
        self.tags_label.setBuddy(self.tags)

        self.retranslateUi(PluginBuilderDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), PluginBuilderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginBuilderDialogBase)
        PluginBuilderDialogBase.setTabOrder(self.class_name, self.title)
        PluginBuilderDialogBase.setTabOrder(self.title, self.description)
        PluginBuilderDialogBase.setTabOrder(self.description, self.module_name)
        PluginBuilderDialogBase.setTabOrder(self.module_name, self.plugin_version)
        PluginBuilderDialogBase.setTabOrder(self.plugin_version, self.qgis_minimum_version)
        PluginBuilderDialogBase.setTabOrder(self.qgis_minimum_version, self.menu_text)
        PluginBuilderDialogBase.setTabOrder(self.menu_text, self.author)
        PluginBuilderDialogBase.setTabOrder(self.author, self.email_address)
        PluginBuilderDialogBase.setTabOrder(self.email_address, self.tracker)
        PluginBuilderDialogBase.setTabOrder(self.tracker, self.homepage)
        PluginBuilderDialogBase.setTabOrder(self.homepage, self.repository)
        PluginBuilderDialogBase.setTabOrder(self.repository, self.tags)
        PluginBuilderDialogBase.setTabOrder(self.tags, self.experimental)
        PluginBuilderDialogBase.setTabOrder(self.experimental, self.button_box)
        PluginBuilderDialogBase.setTabOrder(self.button_box, self.scrollArea)

    def retranslateUi(self, PluginBuilderDialogBase):
        PluginBuilderDialogBase.setWindowTitle(_translate("PluginBuilderDialogBase", "QGIS Plugin Builder 2.0.3", None))
        self.title_label.setText(_translate("PluginBuilderDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">QGIS Plugin Builder</span></p></body></html>", None))
        self.class_name_label.setText(_translate("PluginBuilderDialogBase", "Class name", None))
        self.class_name.setToolTip(_translate("PluginBuilderDialogBase", "This is the Python class name for your plugin.\n"
"It should be in CamelCase e.g. PhotoLinker.", None))
        self.class_name.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. PhotoLinker", None))
        self.plugin_name_label.setText(_translate("PluginBuilderDialogBase", "Plugin name", None))
        self.title.setToolTip(_translate("PluginBuilderDialogBase", "This is the name for your plugin that will be displayed in the QGIS\n"
"Plugin Manager and the Plugins menu e.g. Photo Linker", None))
        self.title.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. Photo Linker", None))
        self.description_label.setText(_translate("PluginBuilderDialogBase", "Description", None))
        self.description.setToolTip(_translate("PluginBuilderDialogBase", "A one-liner description of the plugin that appears in the Plugin\n"
"Manager e.g. \"The photo linker plugin lets you link photos to\n"
"points.\"", None))
        self.description.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. This plugin links points to photos", None))
        self.module_name_label.setText(_translate("PluginBuilderDialogBase", "Module name", None))
        self.module_name.setToolTip(_translate("PluginBuilderDialogBase", "This is the python module name for your plugin. It should be lower case\n"
"underscore separated e.g. photo_linker.", None))
        self.module_name.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. photo_linker", None))
        self.plugin_version_label.setText(_translate("PluginBuilderDialogBase", "Version number", None))
        self.plugin_version.setToolTip(_translate("PluginBuilderDialogBase", "The version of this plugin using semantic versioning (see\n"
"http://semver.org) e.g. 0.1.1", None))
        self.plugin_version.setText(_translate("PluginBuilderDialogBase", "0.1", None))
        self.plugin_version.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. 0.1.0", None))
        self.qgis_minimum_version_label.setText(_translate("PluginBuilderDialogBase", "Minimum QGIS version", None))
        self.qgis_minimum_version.setToolTip(_translate("PluginBuilderDialogBase", "Minimum QGIS minor version required for this plugin to work e.g. 2.0", None))
        self.qgis_minimum_version.setText(_translate("PluginBuilderDialogBase", "2.0", None))
        self.qgis_minimum_version.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. 2.0", None))
        self.menu_text_label.setText(_translate("PluginBuilderDialogBase", "Text for the menu item", None))
        self.menu_text.setToolTip(_translate("PluginBuilderDialogBase", "This is the text that will appear in the menu under your Plugin\n"
"name e.g. Link photos to points.", None))
        self.menu_text.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. Link photos to points", None))
        self.author_label.setText(_translate("PluginBuilderDialogBase", "Author/Company", None))
        self.author.setToolTip(_translate("PluginBuilderDialogBase", "Your name or company name (used in the copyright header) e.g.\n"
"Acme Corp.", None))
        self.author.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. Acme widgets Inc.", None))
        self.email_address_label.setText(_translate("PluginBuilderDialogBase", "Email address", None))
        self.email_address.setToolTip(_translate("PluginBuilderDialogBase", "Your email address (used in the copyright header) e.g. bill@gates\n"
".com", None))
        self.email_address.setPlaceholderText(_translate("PluginBuilderDialogBase", "e.g. bill@gates.com", None))
        self.optional_items_label.setText(_translate("PluginBuilderDialogBase", "Optional Items", None))
        self.tracker_label.setText(_translate("PluginBuilderDialogBase", "Bug tracker", None))
        self.tracker.setToolTip(_translate("PluginBuilderDialogBase", "Url of your plugin\'s bug tracker", None))
        self.homepage_label.setText(_translate("PluginBuilderDialogBase", "Home page", None))
        self.homepage.setToolTip(_translate("PluginBuilderDialogBase", "Url of your plugin\'s home page", None))
        self.repository_label.setText(_translate("PluginBuilderDialogBase", "Repository", None))
        self.repository.setToolTip(_translate("PluginBuilderDialogBase", "Url of your plugin repository (if you have one)", None))
        self.tags_label.setText(_translate("PluginBuilderDialogBase", "Tags", None))
        self.tags.setToolTip(_translate("PluginBuilderDialogBase", "A comma separated list of tags that describe the plugin features or function", None))
        self.experimental.setText(_translate("PluginBuilderDialogBase", "Flag the plugin as experimental", None))

