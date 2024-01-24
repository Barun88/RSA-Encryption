import tkinter as tk
import rsa 
#variables
plain_text='null'
enc_text='null'

#key generation
public_key,private_key = rsa.generate_keypair(16)

#basic functions 
def get_text() :
    plain_text=txt_field.get("1.0","end-1c")
    print(plain_text)
    enc_text=rsa.encrypt(plain_text,public_key)
    filename="commonfile.txt"
    with open(filename, 'w') as file:
         for char in enc_text:
            file.write(str(char) + '\n')
    out_field.insert(tk.END,enc_text)
    file.close()

def open_user2_window():
    newwindow=tk.Toplevel(root)
    newwindow.title('User 2')
    newwindow.geometry('550x400')
    # Open the file
    file_path = 'commonfile.txt'
    with open(file_path, 'r') as file:
        numbers=[int(line.strip()) for line in file]


    label_cipher=tk.Label(newwindow,text='Cipher Text',font=('calibre',10,'bold'))
    cipher_field=tk.Text(newwindow,height=20,width=35,bg='cyan')
    cipher_field.insert(tk.END,numbers)
    dec_text=rsa.decrypt(numbers,private_key)
    label_plaintext=tk.Label(newwindow,text='Plain Text',font=('calibre',10,'bold'))
    ptxt_field=tk.Text(newwindow,height=20,width=35,bg='light pink')
    ptxt_field.insert(tk.END,dec_text)
    print(f"Decrypted Message: {dec_text}")
    #dec_button=tk.Button(newwindow,text='Decrypt',command=None)
    

    label_cipher.grid(row=0,column=0)
    cipher_field.grid(row=1,column=0)
    label_plaintext.grid(row=0,column=1)
    ptxt_field.grid(row=1,column=1)
    #dec_button.grid(row=2,column=0)
    file.close()




#mainframe
root=tk.Tk()
root.title('Encrypt')
root.geometry('550x400')

#menu
menubar=tk.Menu(root)

user2=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Menu',menu=user2)
user2.add_command(label='User 2',command=open_user2_window)
#user2.add_command(label='All Users',command=None)
user2.add_command(label='Exit',command=root.destroy)

#text field for plaintext entry
l=tk.Label(root,text='Enter Plain Text',font=('calibre',10,'bold'))
txt_field=tk.Text(root,height=20,width=35,bg='light pink')

#text field for cipher text
l2=tk.Label(root,text='Cipher Text',font=('calibre',10,'bold'))
out_field=tk.Text(root,height=20,width=35,bg='cyan')


#buttons or any funtion oriented fields
enc_button=tk.Button(root,text='Encrypt',font=('calibre',10,'bold'),command=get_text)

#binding area
l.grid(row=0,column=0)
txt_field.grid(row=1,column=0)
l2.grid(row=0,column=1)
out_field.grid(row=1,column=1)
enc_button.grid(row=2,column=0)



#test area 




#just the main loop
root.config(menu=menubar)
root.mainloop()

