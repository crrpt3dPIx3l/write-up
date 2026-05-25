# SSRF

What is the flag from the /private directory?

Reading the question and understanding the HTML code

![bd9ee9ac0b7592b5343cbc8dd9b57189](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/bd9ee9ac0b7592b5343cbc8dd9b57189.png)

If you choose one of the avatars and then click the **Update Avatar** button, you'll see the form change and, above it, display your currently selected avatar.

![8685bf7a4b24616031425a7f5e8db1ae](https://tryhackme-images.s3.amazonaws.com/user-uploads/5c549500924ec576f953d9fc/room-content/8685bf7a4b24616031425a7f5e8db1ae.png)

Viewing the page source will show your current avatar is displayed using the data URL scheme, and the image content is base64 encoded as per the screenshot below.

![Enlarged image](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/fff0ea113602635dcf5d1e8d0b1d8bca.png)

Now let's try making the request again but changing the avatar value to **private** in hopes that the server will access the resource and get past the IP address block. To do this, firstly, right-click on one of the radio buttons on the avatar form and select **Inspect**:

![Enlarged image](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/2ef87608418e47625bedad9d0361ed08.png)

Be sure to select the avatar you edited and then click the **Update Avatar** button. Unfortunately, it looks like the web application has a deny list in place and has blocked access to the /private endpoint.

![Enlarged image](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/a59460cc19eaf5776ee8a882e25b2d64.png)

As you can see from the error message, the path cannot start with /private but don't worry, we've still got a trick up our sleeve to bypass this rule. We can use a directory traversal trick to reach our desired endpoint. Try setting the avatar value to **x/../private**

![Enlarged image](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/84b88d9c6fa6a29450520625bb42870d.png)

You'll see we have now bypassed the rule, and the user updated the avatar. This trick works because when the web server receives the request for **x/../private**, it knows that the **../** string means to move up a directory that now translates the request to just **/private**.

Viewing the page source of the avatar form, you'll see the currently set avatar now contains the contents from the **/private** directory in base64 encoding, decode this content and it will reveal a flag that you can enter below.

```HTML
<div class="avatar-image" style="background-image: url(data:image/png;base64,VEhNe1lPVV9XT1JLRURfT1VUX1RIRV9TU1JGfQ==)"></div>
```

by decoding the new choosen image and espacially the one we planted the private directory on to reveal the flag it will be displayed once decoded.
