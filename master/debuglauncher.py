import re
import sys
import os

from twisted.scripts.twistd import run
try:
    os.remove('twistd.pid')
except:
    pass
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(run())