# Safe Opener
## Description
Can you open this safe? I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: picoCTF{password}

### Hints
none

## Solution
Starting by downloading the program using the `wget` command, next using the `file SafeOpener.java` to check the characteristics of the file
```
SafeOpener.java: Java source, ASCII text
```
then I opened the code in an IDE to examine the content
```
import java.io.*;
import java.util.*;  
public class SafeOpener {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              
            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }
    
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}
```
after reading the code the encoded password is revealed already in the `openSafe` function in the line 31 `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz` so went back to the code to check If any thing else is important and found that the password is encoded using the `Base64.Encoder` class so I head up to cyberchef to decode the password I got to get `pl3as3_l3t_m3_1nt0_th3_saf3`, wrapping it with the flag format `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`.
PWNED!