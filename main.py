import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    link = link_entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a link.")
        return
    try:
        global qr_img
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=2,
        )
        qr.add_data(link)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        img = qr_img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk
        save_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_qr():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if file_path:
        try:
            qr_img.save(file_path)
            messagebox.showinfo("Success", "QR Code saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save QR Code: {e}")

root = tk.Tk()
root.title("Minimal QR Generator")
root.geometry("300x350")

link_entry = tk.Entry(root, font=("Arial", 12))
link_entry.pack(pady=20, fill=tk.X, padx=20)

generate_button = tk.Button(root, text="Generate", font=("Arial", 12), command=generate_qr)
generate_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

save_button = tk.Button(root, text="Save", font=("Arial", 12), state=tk.DISABLED, command=save_qr)
save_button.pack(pady=10)

root.mainloop()
