# -*- coding: utf-8 -*-
import os

class ImportPlugin(object):
    def __init__(self):
        self.plugins_list = {}
        self.tools_of_category = {}
        self.path = ""
        self.config_path()
        self.parse_config()

    def config_path(self):
        if "plugins" not in os.getcwd():
            self.path = os.getcwd()+"/coffesploit/plugins/"
        else:
            self.path = os.getcwd()

    def getpath(self):
        return self.path

    #read config.ini file load plugins in config
    def parse_config(self):
        try:
            filename = self.path + "config.ini"
            conf = open(filename, "r")
            for line in conf.readlines():
            	# line like: scan,nmap,nmapparser.py,NmapParser
                plugin_type, plugin_name, plugin_file, plugin_class = line.strip().split(",") # if there is \n in line delete it
                self.plugins_list[plugin_name] = plugin_type, plugin_file, plugin_class
                #if self.tools_of_category.get(plugin_type) is None:
                #	self.tools_of_category[plugin_type] = []
                self.tools_of_category.setdefault(plugin_type, []).append(plugin_name)
            conf.close()
        except IOError:
            print ("There is no config.ini in %s" % self.path)
            exit(0)
    
    def get_tools_by_category(self):
    	return self.tools_of_category
    
    def get_tool_categories(self):
    	return self.get_tools_by_category().keys()
    		
    def get_plugins_list(self):
        return self.plugins_list
