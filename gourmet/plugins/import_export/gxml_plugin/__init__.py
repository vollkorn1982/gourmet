from . import gxml_exporter_plugin
from . import gxml_importer_plugin

plugins = [gxml_exporter_plugin.GourmetExporterPlugin,
           gxml_importer_plugin.GourmetXML2Plugin,
           gxml_importer_plugin.GourmetXMLPlugin
           ]
