#include <iostream>
#include <vector>
#include <string>
#include <filesystem>
#include <cstdlib>

void get_file_paths(char const *fname, std::string& fasta_pathname, std::string& faidx_pathname)
{
    std::filesystem::path fasta_path = fname;

    if (!std::filesystem::exists(fasta_path))
    {
        std::cerr << "error: path '" << fname << "' does not exist" << std::endl;
        exit(-1);
    }
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

    return 0;
}
