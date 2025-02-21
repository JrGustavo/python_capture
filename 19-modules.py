import sys
print(sys.path)

import re
text = 'Mi número de teléfono es 123-456-7890'
result = re.findall('[0,9]', text)
print(result)

import time
timestamp = time.time()
print(timestamp)
