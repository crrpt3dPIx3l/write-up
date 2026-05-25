# Binary Instrumentation 2
## Description
I've been learning more Windows API functions to do my bidding. Hmm... I swear this program was supposed to create a file and write the flag directly to the file. Can you try and intercept the file writing function to see what went wrong? Download the exe here. Unzip the archive with the password picoctf 

### Hints
1. Frida is an easy-to-install, lightweight binary instrumentation toolkit
2. Try using the CLI tools like frida-trace
3. You can specify the exact function name you want to trace

## Solution
Starting by downloading the zip file from the challenge, extracting the challange binary `bininst2.exe`. By reading the hints it again says use Frida tools from the "Binary Instrumentation 1".
So I used the commands `frida-trace -f bininst2.exe -i "*"` to trace all the API calls
Next using this command `frida-trace -i *File* -f bininst2.exe -X KERNEL32` I displayed all the API calls that contains the word "File", and thats because the flag is probably is read from a file
```
Instrumenting...

...

Started tracing 547 functions. Web UI available at http://localhost:51013/
           /* TID 0x18bc */
   501 ms  NtDeviceIoControlFile()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   501 ms  NtQueryAttributesFile()
   501 ms  NtQueryAttributesFile()
   501 ms  NtOpenFile()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   511 ms  GetSystemTimeAsFileTime()
   511 ms     | GetSystemTimeAsFileTime()
   511 ms  GetModuleFileNameW()
   511 ms     | GetModuleFileNameW()
   511 ms  AreFileApisANSI()
   511 ms     | AreFileApisANSI()
   511 ms  CreateFileA()
   511 ms     | CreateFileA()
```
So after knowing that there is a funciton for creating a file now, the script for creating a file should be added there and this is because if the function already has a body code it would execute but it does nothing so I pass the code for making a file
```
HANDLE CreateFileA(
  [in]           LPCSTR                lpFileName,
  [in]           DWORD                 dwDesiredAccess,
  [in]           DWORD                 dwShareMode,
  [in, optional] LPSECURITY_ATTRIBUTES lpSecurityAttributes,
  [in]           DWORD                 dwCreationDisposition,
  [in]           DWORD                 dwFlagsAndAttributes,
  [in, optional] HANDLE                hTemplateFile
);
```
The code is obtained from microsoft [website](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea)
By modifying the obtained code from microsoft to 
```
defineHandler({
  onEnter(log, args, state) {
    // Read original filename
    state.originalPath = Memory.readUtf8String(args[0]);
    log('CreateFileA - Original path: "' + state.originalPath + '"');
    
    // Replace the invalid path with a valid one
    const newPath = Memory.allocUtf8String('flag.txt');
    args[0] = newPath;
    
    // Save reference to prevent garbage collection
    state.newPath = newPath;
    
    log('CreateFileA - Replaced with: "flag.txt"');
  },
  
  onLeave(log, retval, state) {
    log('CreateFileA returned: ' + retval);
  }
});
```
With the help of ChatGpt and run the command `frida-trace -i CreateFileA -f bininst2.exe -X KERNEL32` a flag.txt file was created but it was empty, but the CreateFileA funciton was working.
I modified the WriteFile function in order to write the flag in the file,
from the same place I got the CreateFileA I've got WriteFile.
```
BOOL WriteFile(
  [in]                HANDLE       hFile,
  [in]                LPCVOID      lpBuffer,
  [in]                DWORD        nNumberOfBytesToWrite,
  [out, optional]     LPDWORD      lpNumberOfBytesWritten,
  [in, out, optional] LPOVERLAPPED lpOverlapped
);
```
Then I modified it to
```
{
  onEnter(log, args, state) {
    // Log basic info
    log('WriteFile called with handle: ' + args[0]);
    log('WriteFile buffer content:');
    log(hexdump(args[1]));
  },
  
  onLeave(log, retval, state) {
    // Log result
    log('WriteFile returned: ' + retval);
  }
}
```
Then I run the program again to check the progress
```
frida-trace -i CreateFileA -i WriteFile -f bininst2.exe -X KERNEL32

Instrumenting...
CreateFileA: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNELBASE.dll\CreateFileA.js"
WriteFile: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNELBASE.dll\WriteFile.js"
CreateFileA: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNEL32.DLL\CreateFileA.js"
WriteFile: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNEL32.DLL\WriteFile.js"
Started tracing 4 functions. Web UI available at http://localhost:49342/
           /* TID 0x1838 */
    20 ms  CreateFileA()
    20 ms     | CreateFileA - Original path: "<Insert path here>"
    20 ms     | CreateFileA - Replaced with: "flag.txt"
    20 ms  CreateFileA returned: 0x270
    20 ms  WriteFile()
    20 ms     | WriteFile called with handle: 0x270
    20 ms     | WriteFile buffer content:
    20 ms     |             0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
140002270  63 47 6c 6a 62 30 4e 55 52 6e 74 6d 63 6a 46 6b  cGljb0NURntmcjFk
140002280  59 56 39 6d 4d 48 4a 66 59 6a 46 75 58 32 6c 75  YV9mMHJfYjFuX2lu
140002290  4e 58 52 79 64 57 30 7a 62 6e 51 30 64 47 6c 76  NXRydW0zbnQ0dGlv
1400022a0  62 69 46 66 59 6a 49 78 59 57 56 6d 4d 7a 6c 39  biFfYjIxYWVmMzl9
1400022b0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
1400022c0  40 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00  @...............
1400022d0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
1400022e0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
1400022f0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002300  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002310  00 00 00 00 00 00 00 00 00 30 00 40 01 00 00 00  .........0.@....
140002320  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002330  a0 21 00 40 01 00 00 00 b0 21 00 40 01 00 00 00  .!.@.....!.@....
140002340  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002350  00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002360  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
    20 ms  WriteFile returned: 0x1
Process terminated

```
And it was working well and file contained the value `cGljb0NURntmcjFkYV9mMHJfYjFuX2luNXRydW0zbnQ0dGlvbiFfYjIxYWVmMzl9` which is the flag but in base64 form, decoded flag: `picoCTF{fr1da_f0r_b1n_in5trum3nt4tion!_b21aef39}`