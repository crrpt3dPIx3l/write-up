# Safe Opener 2
## Description
What can you do with this file? I forgot the key to my safe but this file is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

### Hints
Download and try to decompile the file.

## Solution
Starting by downloading the file and examining the content of `SafeOpener.class`
```
// Source code is decompiled from a .class file using FernFlower decompiler (from Intellij IDEA).
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Base64;

public class SafeOpener {
   public SafeOpener() {
   }

   public static void main(String[] args) throws IOException {
      BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
      Base64.Encoder encoder = Base64.getEncoder();
      String encodedkey = "";
      String key = "";

      for(int i = 0; i < 3; ++i) {
         System.out.print("Enter password for the safe: ");
         key = keyboard.readLine();
         encodedkey = encoder.encodeToString(key.getBytes());
         System.out.println(encodedkey);
         boolean isOpen = openSafe(encodedkey);
         if (isOpen) {
            break;
         }

         System.out.println("You have  " + (2 - i) + " attempt(s) left");
      }

   }

   public static boolean openSafe(String password) {
      String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_5bfbd6f1}";
      if (password.equals(encodedkey)) {
         System.out.println("Sesame open");
         return true;
      } else {
         System.out.println("Password is incorrect\n");
         return false;
      }
   }
}
```

the flag is in the open source code
PWNED!