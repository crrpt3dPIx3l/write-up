var k32 = Module.findExportByName("kernel32.dll", "Sleep")  
  
if (k32) {  
       Interceptor.replace(k32, new NativeCallback(function(ms) {  
               console.log("Sleep Intercepted!")  
               return // Skip the sleep  
       }, "void", ["uint32"]))  
}
