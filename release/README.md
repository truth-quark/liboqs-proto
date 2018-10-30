liboqs-proto Release Utils
==========================

The prototype tools here are:

- **check_kem_example.py:** Requires 'meld' diff viewer. Automatically extracts the KEM wiki page code block and compares it against the example_kem.c file in the liboqs repo (nist or master branch, whichever is checked out).
- **check_sig_example.py:** Also requires 'meld'. Extracts the SIG code block from the wiki page and compares it against the example_sig.c file (nist or master branch).

**TODO**: merge the scripts in one... with a KEM|SIG arg