# -*- coding: utf-8 -*-
import importlib
import sys
from coffesploit.core.pluginmanage.importplugin import ImportPlugin
#from coffesploit.core.pluginmanage.resultplugin import run_result

class PluginManager(object):
    """该类负责加载插件,提供插件运行和插件结果函数.
    The Class is designed to load plugin at runtime,
    and give api to run the plugin ,get the result of the plugin.
    """
    
    def __init__(self):
        self.current_plugin_name = None
        self.current_plugin_file = None
        self.current_plugin_class = None
        self.current_plugin_type = None
        self.current_plugin = None
        self.status = None
        self.importer = ImportPlugin()

    def set_current_plugin_name(self, plugin_name):
        """if plugin name is in config file set plugin name
        调用importer的函数从配置文件中读取插件名称
        """
        plugin_list = self.get_plugins_list()
        if plugin_name in plugin_list:
            self.current_plugin_name = plugin_name
            self.current_plugin_type, self.current_plugin_file, self.current_plugin_class = plugin_list[plugin_name]
            return ''
        else:
            return('no such plugin\n')
	
    def get_tools_by_category(self):
    	return self.importer.get_tools_by_category()
    	
    def get_tool_categories(self):
    	return self.importer.get_tool_categories()
    
    def get_plugins_list(self):
    	return self.importer.get_plugins_list()
    	
    def load_plugin(self, plugin):
        """set path to load plugin
        	从importplugin 中获取插件所在绝对路径,使用import_moudle加载
        """
        intermediateInfo = self.set_current_plugin_name(plugin)            
        importfile = "coffesploit.plugins." + self.current_plugin_type + "." + self.current_plugin_file[0:-3]	
        try:
            module = importlib.import_module(importfile)
        except ImportError:
            module = None
            logmanager.puttolog("can't import : " + importfile)
        pluginClass = getattr(module, self.current_plugin_class, None)
        if pluginClass is not None:
        	self.current_plugin = pluginClass()
	        self.status = self.current_plugin.status()
		return intermediateInfo
		
    def plugin_run(self):
        """run current plugin"""
        if self.current_plugin is not None:
            self.current_plugin.run(self.status)
            #run_result.log_result(self.plugin_result())
            return True
        else:
        	return("You should choose a tool before do this!")

    def plugin_result(self):
		"""get the result of the plugin"""
		if self.current_plugin is not None:
			return self.current_plugin.result()
		else:
			return self.current_plugin_name, "Reslut is None"			# return a tuple

    def plugin_status(self):
        return self.status
        
    def set_args(self, *args):
        if len(args) == 2 and args[0] in self.status:
            self.status[args[0]] = args[1]
            
    def plugin_help(self):
		return self.current_plugin.help()
