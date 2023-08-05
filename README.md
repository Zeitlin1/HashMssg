# HashMssg
 A script to verify a sender's message is authentic

 Directions:
 First, run the PEM generator script "PEMGen.py", this will generate 2x random PEM keys, a private key (used for signing) and a public key (used for verifying messages). The public key can be given out to those who wish to verify messages from the author.  The private key should be kept hidden from public view at all times.

 $ python3 PEMGen.py

 ![image](https://github.com/Zeitlin1/HashMssg/assets/21022488/ca8af2cb-3dd9-4b8b-8178-7f27fea03491)

 Then, run the "pyHashgui.py" script which will bring up the user interface allowing you to sign and check messages.

 $ python3 pyHashgui.py

 ![image](https://github.com/Zeitlin1/HashMssg/assets/21022488/509adba1-c588-4d33-a0f9-5109436c4a8d)

 Use the private PEM key to digitally sign your message (be sure to inclue the -----BEGIN PRIVATE KEY----- & -----END PRIVATE KEY----- in the key textfields).  Signing the message will create a signature using the private PEM key and the message as inputs.  The signature should be included with published messages for later verification.  

 ![image](https://github.com/Zeitlin1/HashMssg/assets/21022488/d1d2b7cc-6417-4828-8137-aa7c184d44c0)

 To verify if a message is authentic and unchanged, simply paste in the signature generated from the author's message and the author's alleged message.

 ![image](https://github.com/Zeitlin1/HashMssg/assets/21022488/ddd144fa-b814-4b53-ab92-90e24ec90e57)

 Click "Verify Signature" and if the message is authentic, the result will be "True".  If any changes have been made to the message or the signature, the result will be "False".

 

 
