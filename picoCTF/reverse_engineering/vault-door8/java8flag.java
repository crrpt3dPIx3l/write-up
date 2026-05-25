import java.util.*;

class java8flag {
    public static void main(String[] args) {

        char[] expected = {
            0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4,
            0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86,
            0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xA4,
            0xA4, 0xA4, 0xD1, 0xE1, 0xC2, 0xB4, 0xA4, 0xF1
        };

        char[] result = descramble(new String(expected));
        System.out.println(String.valueOf(result));
    }

    public static char[] descramble(String input) {
        char[] arr = input.toCharArray();

        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];

            // reverse order of scramble()
            c = swap(c, 6, 7);
            c = swap(c, 2, 5);
            c = swap(c, 3, 4);
            c = swap(c, 0, 1);
            c = swap(c, 4, 7);
            c = swap(c, 5, 6);
            c = swap(c, 0, 3);
            c = swap(c, 1, 2);

            arr[i] = c;
        }
        return arr;
    }

    public static char swap(char c, int p1, int p2) {
        char m1 = (char)(1 << p1);
        char m2 = (char)(1 << p2);

        char b1 = (char)(c & m1);
        char b2 = (char)(c & m2);

        char rest = (char)(c & ~(m1 | m2));
        int shift = p2 - p1;

        return (char)((b1 << shift) | (b2 >> shift) | rest);
    }
}
