import sys
import os
PATH = os.pathsep.join(
    (os.path.dirname(sys.executable),os.environ["PATH"])
    )

print(PATH)
