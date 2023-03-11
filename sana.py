import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from test64 import riaz

    riaz()

elif bit == '32bit':

    from test32 import riaz

    riaz()