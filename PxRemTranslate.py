import sublime, sublime_plugin,re,math

class pxtoremeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            if not region.empty():


                # retrieve the settings
                self.settings = sublime.load_settings('Test.sublime-settings')
                base_rem = self.settings.get('1rem', 16)

                # get the selected text
                s = view.substr(region)

                p = re.compile("(((?<=[{;\n\s])*.*):(.*(px|em|%|0)(?=(;|\n|}))))")

                for com in p.finditer(s):

                    old = com.group(3)
                    attr = []
                    
                    old = re.sub("^(\n|\s|\r)+",'',old)
 
                    for a in re.split('\s',old):
                    	unit = a[-2:]
                    	if unit == 'px':        	
	                    	n = a.replace('px','')                    	
	                    	rem = float(n) / base_rem
	                    	rem = '{0:g}'.format(rem)
	                    	attr.append(str(rem) + 'rem')
                    	else:
                    		attr.append(a)


                    result = ' '.join(attr) 
                    s = s.replace(old,result,1)       

                
                view.replace(edit,region,s)


class remtopxeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            if not region.empty():


                # retrieve the settings
                self.settings = sublime.load_settings('Test.sublime-settings')
                base_rem = self.settings.get('1rem', 16)

                # get the selected text
                s = view.substr(region)

                p = re.compile("(((?<=[{;\n\s])*.*):(.*(rem|em|%|0)(?=[;\n}])))")

                for com in p.finditer(s):

                    old = com.group(3)
                    attr = []
                    old = re.sub("^(\n|\s|\r)+",'',old)
 
                    for a in re.split('\s',old):  
                    	unit = a[-3:]
                    	if unit == 'rem':
	                    	n = a.replace('rem','');
	                    	rem = float(n) * base_rem

	                    	rem = '{0:g}'.format(rem)
	                    	attr.append(str(rem) + 'px')
                    	else:
                    		attr.append(a)

                    result = ' '.join(attr)                   

                    s = s.replace(old,result,1)       

                
                view.replace(edit,region,s)