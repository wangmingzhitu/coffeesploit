# -*- coding: utf-8 -*-

class HelpManager(object):
	"""class to print help informations help users use coffesploit"""
	
	def __init__(self):
		self.help_list = {"use": self.help_use, "tools": self.help_plugins,
						  "set": self.help_set, "run": self.help_run,
						  "help": self.main_help, "exit": self.help_exit,
						  "version": self.help_version, "banner": self.help_banner,
						  "update": self.help_update
						  }
						  
	def help_use(self):
		return("Description: determin to use wihch tool.\n" +
			  "Usage: use <tool>\n" +
			  "exp: use nmap\n")
			
	def help_set(self):
		return("Description: used to set current tool's arguments\n" +
			  "Usage: set key value\n" +
			  "exp: set hosts 127.0.0.1\n" +
			  "     set ports 20-400\n")
			
	def help_plugins(self):
		return("Description: there are two usages about the command:\n" +
			  "Usage1:\n" +
			  "    tools --> Show all available tools currently\n" +
			  "Usage2:\n" +
			  "    tools <tool> help --> Show how to use the 'tool'.Attention,you should load it before do this,use 'use' command to do.\n" +
			  "    Exp: tools nmap help\n")
			
	def help_run(self):
		return("Description: start run the tool that you choose.\n" +
			  "Usage: run\n")
	
	def help_exit(self):
		return("Description: exit current process.\n" +
			  "Usage: exit\n")
			  
	def help_update(self):
		return("Description: update tools list.\n" +
			  "Note: you should ensure both tool-package's, tool-moudle's name are the same as tool-class's, just like in Java.\n" +
			  "Usage: update\n")
		
	def help_version(self):
		return("Description: show current version.\n" +
			  "Usage: version\n")
		
	def help_banner(self):
		return("Description: show baner.\n" +
			  "Usage: version\n")
			  		
	def main_help(self):
		return("Welcome to Coffesploit, input 'help <command>' to show detailed usage of the 'command'\n" +
			  "Usage: help <command>\n" +
			  "Exp: help use\n\n" +
			  "some basic <commands> are as follows:\n\n" +
			  "use --> Determin to use which tool\n" +
			  "run --> Run the tool you choosed\n" +
			  "set --> Used to set current tool's arguments\n" +
			  "update --> Update all tools\n" +
			  "tools --> Display all available tools currently or show one tool's usage after loaded it.\n"+
			  "help --> Show all help information\n" +
			  "exit --> Finish all work\n" +
			  "version --> Show current version\n" +
			  "banner --> Show banner\n")
			
	def gethelp(self, arg):
		if arg in self.help_list:
			return(self.help_list[arg]())
		else:
			return("no help information about %s\n" %arg)
			
