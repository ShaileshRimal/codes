import platform
import os
# bit=platform.architecture()[0]
# print(bit)


name=os.name
platformm=platform.system()
releasee=platform.release()
print(name,platformm ,releasee)