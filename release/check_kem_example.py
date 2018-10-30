import os
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    usage = 'USAGE: check_kem_example.py <liboqs-repo-path>'
    sys.exit(usage)

liboqs_path = sys.argv[1]
nist_example_path = os.path.join(liboqs_path, 'src/kem/example_kem.c')
assert os.path.exists(nist_example_path)

url = 'https://github.com/open-quantum-safe/liboqs/wiki/Minimal-example-of-a-post-quantum-key-encapsulation-mechanism'
resp = requests.get(url)
resp.raise_for_status

html_txt = resp.content
soup = BeautifulSoup(html_txt, features='lxml')
txt = soup.get_text()

start_str = 'Below is a minimal example of a post-quantum key encapsulation implemented in liboqs (using the nist-branch).'
start = txt.index(start_str)
end = txt.index('To compile the above example in a POSIX-like environment')
code = txt[start + len(start_str)+1:end] 

dest_path = '/tmp/kem_code_example.c'
with open(dest_path, 'w') as f:
	f.write(code)

os.system('meld {} {} &'.format(dest_path, nist_example_path))
