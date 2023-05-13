#!/usr/bin/env python

import sys
from pathlib import Path

def get_file_paths(path):
    fasta_path = Path(path)
    if not fasta_path.exists():
        sys.stderr.write("error: path '{}' does not exist\n".format(path))
        sys.stderr.flush()
        sys.exit(-1)
    if not fasta_path.is_file():
        sys.stderr.write("error: path '{}' does not reference a file\n".format(path))
        sys.stderr.flush()
        sys.exit(-1)
    faidx_path = fasta_path.with_suffix(fasta_path.suffix + ".fai")
    if faidx_path.exists():
        sys.stderr.write("path '{}' already exists, nothing to do\n".format(str(faidx_path)))
        sys.stderr.flush()
        sys.exit(0)
    return fasta_path, faidx_path

def main(argc, argv):

    if argc != 2:
        sys.stderr.write("usage: {} <reads.fa>\n".format(argv[0]))
        sys.stderr.flush()
        return -1

    fasta_path, faidx_path = get_file_paths(argv[1])

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
