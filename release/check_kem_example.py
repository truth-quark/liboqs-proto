import os
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    usage = 'USAGE: check_kem_example.py <liboqs-repo-path>'
    sys.exit(usage)

liboqs_path = sys.argv[1]
example_path = os.path.join(liboqs_path, 'src/kem/example_kem.c')

if not os.path.exists(example_path):
	example_path = os.path.join(liboqs_path, 'tests/example_kem.c')
	assert os.path.exists(example_path)

url = 'https://github.com/open-quantum-safe/liboqs/wiki/Minimal-example-of-a-post-quantum-key-encapsulation-mechanism'
resp = requests.get(url)
resp.raise_for_status

html_txt = resp.content
soup = BeautifulSoup(html_txt, features='lxml')
txt = soup.get_text()

start_str = '/*\n * example_kem.c'
end_str = 'OQS_KEM_free(kem);\n}'
start = txt.index(start_str)
end = txt.index(end_str)
code = txt[start:end + len(end_str)+1]

dest_path = '/tmp/wiki_kem_code_example.c'
with open(dest_path, 'w') as f:
	f.write(code)

os.system('meld {} {} &'.format(dest_path, example_path))
