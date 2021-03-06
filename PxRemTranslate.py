import sublime, sublime_plugin,re,math

class pxtoremeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            if not region.empty():


                # retrieve the settings
                self.settings = sublime.load_settings('PxRemTranslate.sublime-settings')
                base_rem = self.settings.get('1rem', 16)

                # get the selected text
                s = view.substr(region)


                p = re.compile("([-\.\d]+)(?=px)px")


                for com in p.finditer(s):

                    a = com.group()
                    old = com.group()

                    n = a.replace('px','')    
                    rem = float(n) / base_rem
                    rem = '{0:g}'.format(rem) + 'rem'
                    s = s.replace(old,rem,1)


                
                view.replace(edit,region,s)






class remtopxeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            if not region.empty():

                # retrieve the settings
                self.settings = sublime.load_settings('PxRemTranslate.sublime-settings')
                base_rem = self.settings.get('1rem', 16)

                # get the selected text
                s = view.substr(region)

                p = re.compile("([-\.\d]+)(?=rem)rem")


                for com in p.finditer(s):

                    a = com.group()
                    old = com.group()

                    n = a.replace('rem','')    
                    rem = float(n) * base_rem
                    rem = '{0:g}'.format(rem) + 'px'
                    s = s.replace(old,rem,1)

                
                view.replace(edit,region,s)
