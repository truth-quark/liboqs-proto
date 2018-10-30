import os
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    usage = 'USAGE: check_sig_example.py <liboqs-repo-path>'
    sys.exit(usage)

liboqs_path = sys.argv[1]
example_path = os.path.join(liboqs_path, 'src/sig/example_sig.c')

if not os.path.exists(example_path):
	example_path = os.path.join(liboqs_path, 'tests/example_sig.c')
	assert os.path.exists(example_path)

url = 'https://github.com/open-quantum-safe/liboqs/wiki/Minimal-example-of-a-post-quantum-signature-in-liboqs'
resp = requests.get(url)
resp.raise_for_status

html_txt = resp.content
soup = BeautifulSoup(html_txt, features='lxml')
txt = soup.get_text()

start_str = 'Below is a minimal example of a post-quantum signature method implemented in liboqs.'
start = txt.index(start_str)
end = txt.index('To compile the above example in a POSIX-like environment')
code = txt[start + len(start_str)+1:end]

dest_path = '/tmp/wiki_sig_code_example.c'
with open(dest_path, 'w') as f:
	f.write(code)

os.system('meld {} {} &'.format(dest_path, example_path))
