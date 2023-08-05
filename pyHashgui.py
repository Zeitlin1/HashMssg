
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.exceptions import InvalidSignature
import base64


# Functions for RSA digital signature
def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    return base64.b64encode(signature)

def verify_signature(public_key, message, signature):
    signature = base64.b64decode(signature)
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False


# GUI callbacks
def on_sign_click():
    private_key_pem = private_key_text.get("1.0", "end").encode()
    message = message_text.get("1.0", "end").encode()

    try:
        private_key = load_pem_private_key(private_key_pem, None)
        signature = sign_message(private_key, message)
        signature_text.delete("1.0", "end")
        signature_text.insert("1.0", signature.decode())
    except ValueError:
        signature_text.delete("1.0", "end")
        signature_text.insert("1.0", "Invalid private key")

def on_verify_click():
    public_key_pem = public_key_text.get("1.0", "end").encode()
    message = verify_message_text.get("1.0", "end").encode()
    signature = verify_signature_text.get("1.0", "end").encode()

    try:
        public_key = load_pem_public_key(public_key_pem)
        is_valid = verify_signature(public_key, message, signature)
        result_text.delete("1.0", "end")
        result_text.insert("1.0", f"Is signature valid? {is_valid}")
    except ValueError:
        result_text.delete("1.0", "end")
        result_text.insert("1.0", "Invalid public key")


# Create the main window
tk = Tk()

tk.title("RSA Digital Signature")

my_label = Label(tk, text = 'Hey World!')

my_label.pack()


# Create labels, entry widgets, and buttons
private_key_label = Label(tk, text="Private Key (PEM format):")
private_key_text = ScrolledText(tk, width=80, height=5)

private_key_label.pack()
private_key_text.pack()



message_label = Label(tk, text="Message:")
message_text = ScrolledText(tk, width=80, height=5)


message_label.pack()
message_text.pack()

signature_label = Label(tk, text="Signature:")
signature_text = ScrolledText(tk, width=80, height=5)

signature_label.pack()
signature_text.pack()


sign_button = Button(tk, text="Sign Message", command=on_sign_click)
sign_button.pack()

public_key_label = Label(tk, text="Public Key (PEM format):")
public_key_text = ScrolledText(tk, width=80, height=5)

verify_message_label = Label(tk, text="Message to verify:")
verify_message_text = ScrolledText(tk, width=80, height=5)

verify_signature_label = Label(tk, text="Signature to verify:")
verify_signature_text = ScrolledText(tk, width=80, height=5)

verify_button = Button(tk, text="Verify Signature", command=on_verify_click)

result_label = Label(tk, text="Verification Result:")
result_text = ScrolledText(tk, width=80, height=2)


# Add widgets to the main window and start the main loop

public_key_label.pack()
public_key_text.pack()
verify_message_label.pack()
verify_message_text.pack()
verify_signature_label.pack()
verify_signature_text.pack()
verify_button.pack()
result_label.pack()
result_text.pack()

tk.mainloop()