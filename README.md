# Visual-Crypto-for-Password-Enhancing
**INTRODUCTION**
<br>
This cryptographic scheme is completely different from the existing one, where the user ID of text type is transformed into the two encrypted images. The server will have a user ID and one of the encrypted image, user sends the another image to the server when it needs to login then the server extracts the ID by making use of OCR (Optical Character Recognition). Finally by comparing the extracted ID with the saved one the exact user is identified. This scheme helps in authentication prevents cyber attack and has low computation when compared with other schemes.
<br>
**ENCRYPTION**
<br>
To build the shared images, first we need to prepare an original image along with a secret message. It is composed of white background and black letter.  The patterns of 4 sub pixels are arranged into 2x2 array format for encryption. The half of the pattern of sub pixels are filled with black and rest half becomes transparent. It can form 6 patterns such as horizontal vertical and diagonal. VC converts each and every pixel to the original image, once the VC based original image is formed the sub pixels become as noise. The shared images are the combination of collected patterns. In shared image the background pixel and message must be different from each other.
The patterns are randomly determined by the pattern numbers. The second shared image pixel position should be same as that of first image which finally represents the background as grey with a mixed form of white and black. <br>
Similarly message part in the shared image is completely opposite of background pixel representation. The first image sub pixels position should be in antitypical format for the second shared image. These images overlap with each other and message are represented in black or white. <br>
First shared image and the second shared image appear as gray as shown in figure 1 and when they overlap with each other the message are displayed in black, but these shared images does not reveal message until they overlap with each other. If the shared image does not match with each other then the message may not be revealed.
<br>
**DECRYPTION**
<br>
To recognize the character overlapped in image we make use of a technique called OCR. OCR is a character recognition technique or algorithm that is used to convert the printed text into text by making use of OCR user is able to recognize the text from the pictures there are few algorithms specifies the OCR. Basic OCR algorithm is a template matching technique were algebraic values are added to acquire the letter that are present within the segment of input characters. Other method is not based on mathematical rule to recognize the various font based characters. <br>
Tesseract is an OCR engine with support for Unicode and the ability to recognize more than 100 languages out of the box.
<br>
**CONCLUSION**
<br>
Enhanced password processing scheme has certain difference when compared to traditional hash based scheme. In this scheme VC is used instead of hash based text, even though the input value is password but the output value is user’s ID as in traditional scheme. At last for authentication user sends only one image to the server having ID and password. There are certain advantages based on these features:
<br>
•	Prevents cyber attack using vulnerable points of hash function. <br>
•	Lower computational cost. <br>
•	Supporting privacy of users. <br>
By using VC random pattern number per pixels are generated for encryption. Generation random number has lower computational complexity than hash function because a pseudorandom number is obtained just by repeating exclusive-or (XOR). <br>
This scheme is mostly used to prevent cyber attack such as brute force attack and dictionary attack as that often occurs in hash based scheme. Even if the attackers hack the saved image he or she may not be able to extract the original password because they are in the form of array of sub pixels. Even if the shared images are expanded and viewed the hackers may not get the entire information it resembles just like a mosaic model. Even if the attackers knew that it is made of certain shapes but they cannot identify what it  is and how the patterns are arranged. <br>
Lastly, this scheme supports the privacy of user. The server saves only one shared image instead of the password and receives another shared image not to expose ID from user. As a result, no information of user such as ID or password is revealed in each shared image.
<br>
**REFERENCE**
<br>
Hamsalatha J, Alisha Erum K, Janani G S “Implementation of Visual Cryptography and OCR Techniques for Processing the Enhanced Password Mechanism”, ird India, ISSN(Online): 2347-2820, Volume -6, Issue-1_2, 2018




