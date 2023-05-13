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
        sys.stderr.write("path '{}' already exists, overwriting\n".format(str(faidx_path)))
        sys.stderr.flush()
        faidx_path.unlink()
    return fasta_path, faidx_path

def main(argc, argv):

    if argc != 2:
        sys.stderr.write("usage: {} <reads.fa>\n".format(argv[0]))
        sys.stderr.flush()
        return -1

    fasta_path, faidx_path = get_file_paths(argv[1])

    fasta_handler = open(str(fasta_path), "r")
    faidx_handler = open(str(faidx_path), "w")

    name = ""
    fpos = foffset = readlen = linelen = 0

    for line in fasta_handler.readlines():
        assert line[-1] == "\n"
        if line[0] == ">":
            if readlen > 0:
                faidx_handler.write("{}\t{}\t{}\t{}\t{}\n".format(name, readlen, fpos, linelen-1, linelen))
                readlen = 0
            name = line.lstrip(">").split()[0].rstrip()
        else:
            if readlen == 0:
                fpos = foffset
                linelen = len(line)
            readlen += len(line)-1
        foffset += len(line)

    if readlen > 0:
        faidx_handler.write("{}\t{}\t{}\t{}\t{}\n".format(name, readlen, fpos, linelen-1, linelen))

    fasta_handler.close()
    faidx_handler.close()

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
