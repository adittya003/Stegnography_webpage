from stegano import lsb
from PIL import Image
import os
from cryptography.fernet import Fernet

def convert_to_png(input_file, output_file):
    if input_file.lower().endswith('.jpg') or input_file.lower().endswith('.jpeg'):
        img = Image.open(input_file)
        png_output_file = output_file
        if not output_file.lower().endswith('.png'):
            png_output_file = os.path.splitext(output_file)[0] + '.png'
        img.save(png_output_file, format='PNG')
        print(f"Converted '{input_file}' to PNG format: '{png_output_file}'")
    else:
        print(f"The input file '{input_file}' is not a JPEG image. No conversion needed.")

def steg_encode(image_path, message, output_path):
    sec = lsb.hide(image_path, message)
    sec.save(output_path)

def steg_decode(image_path):
    msg = lsb.reveal(image_path)
    if msg is not None:
        return msg
    else:
        return "No hidden message found"

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# convert_to_png("pic.jpg","stginput.png")
# message="messi is the best"
# key=generate_key()
# print("Generated key:", key.decode())
# enc_msg=encrypt_message(message,key)
# steg_encode("stginput.png",enc_msg.decode(),"encostginput.png")
# msg=steg_decode("encostginput.png")
# dec_msg=decrypt_message(msg.encode(),key)
# print(dec_msg)

# os.remove("stginput.png")
# os.remove("encostginput.png")