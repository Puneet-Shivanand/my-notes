import sys
import pyinotify

path = sys.argv[1]
outfile = sys.argv[2]
path_to_watch = list(sys.argv[1].split(','))

f = open(outfile,'a')

watch_me = pyinotify.WatchManager()  
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE 

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
	f.write("File Created:"+ event.pathname)
    
handler = EventHandler()
notifier = pyinotify.Notifier(watch_me, handler)
for path in path_to_watch:
	wdd = watch_me.add_watch(path, mask, rec=False)

notifier.loop()