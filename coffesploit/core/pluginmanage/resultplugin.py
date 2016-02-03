# -*- coding: utf-8 -*-
#from coffesploit.core.logmanager import logmanager

class ResultPlugin(object):
	"""
		The class is use to log executive outcomes of current plugin. 
	"""	
	def get_result_for_text(self, outcomes):					# outcomes need to be a dict-like.
		def format_outcomes(result, outcomes, tab_count):
			for key, value in outcomes.iteritems():
				if not value:
					continue
				if issubclass(type(value), dict):
					result += "\n" + "    "*tab_count + '----' + str(key)
					result = format_outcomes(result, value, tab_count + 1)
				else:
					result += "\n" + "    "*tab_count + '----' + str(key) + ": " + str(value)
			return result
		return format_outcomes("", outcomes, 0)
	
	def get_result_for_visual(self, outcomes, toolName):		# outcomes need to be a dict-like.
		def format_outcomes(result, outcomes):
			for key, value in outcomes.iteritems():
				if not value:
					continue
				if issubclass(type(value), dict):
					result['children'].append({'name': str(key), 'children': []})
					result['children'][-1] = format_outcomes(result['children'][-1], value)
				else:
					result['children'].append({'name': str(key), 'children': [{'name': str(value)}]})
			return result			
		result = [{'name': str(toolName), 'children': []}]
		result[-1] = format_outcomes(result[-1], outcomes)
		return result
		
run_result = ResultPlugin()

if __name__ == '__main__':
	outcomes = {'nmap': {u'扫描状态': {'uphosts': u'1', 'timestr': u'Wed Jan 13 16:12:57 2016',  'elapsed': u'6.63'}, '扫描信息': {u'tcp': {'services': u'1,3-4,6-7,9,13,17,19-26,30,32-33,37'}}}}
	print run_result.get_result_for_text(outcomes)
	print "="*40
	print run_result.get_result_for_visual(outcomes,'tool')
