import os
import platform

print(os.name)
print(platform.system())
#print(platform.release())

if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
    do_windows_stuff()
elif sys.platform.startswith('darwin'):
    do_osx_stuff()
elif sys.platform.startswith('linux'):
    do_linux_stuff()
else:
    raise Exception("Nobody's written the stuff for {}, sorry".format(sys.platform))