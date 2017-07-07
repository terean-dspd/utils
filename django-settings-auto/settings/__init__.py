import sys
if sys.argv[1] == 'runserver':
    from .settings_development import *
    print('''
#########################################
#  Development configuration is loaded  #
#########################################
''')
else:
    from .settings_productions import *
try:
   from .site_settings import *
except:
   pass
