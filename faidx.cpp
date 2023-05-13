#include <iostream>
#include <vector>
#include <string>
#include <filesystem>
#include <iomanip>
#include <cstdlib>

namespace fs = std::filesystem;

void get_file_paths(char const *fname, std::string& fasta_pathname, std::string& faidx_pathname)
{
    fs::path fasta_path = fname;

    if (!fs::exists(fasta_path))
    {
        std::cerr << "error: path " << std::quoted(fname) << " does not exist" << std::endl;
        exit(-1);
    }

    if (!fs::is_regular_file(fasta_path))
    {
        std::cerr << "error: path " << std::quoted(fname) << " does not reference a file" << std::endl;
        exit(-1);
    }

    fs::path faidx_path = std::string(fname) + ".fai";

    if (fs::exists(faidx_path))
    {
        std::cerr << "path " << std::quoted(faidx_path.string()) << " already exists, overwriting" << std::endl;
        fs::remove(faidx_path);
    }

    fasta_pathname = fasta_path.string();
    faidx_pathname = faidx_path.string();
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        std::cerr << "usage: " << argv[0] << " <reads.fa>" << std::endl;
        return -1;
    }

    std::string fasta_pathname, faidx_pathname;
    get_file_paths(argv[1], fasta_pathname, faidx_pathname);

    std::cout << std::quoted(fasta_pathname) << "\n" << std::quoted(faidx_pathname) << std::endl;

    return 0;
}
