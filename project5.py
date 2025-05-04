#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox, filedialog

def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    words = text.split()
    return ' '.join(words[::-1])

def save_to_file(text):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
            messagebox.showinfo("Success", f"Text saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def gui_reverse(mode):
    input_text = entry.get()
    if not input_text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    if mode == "char":
        result = reverse_characters(input_text)
    else:
        result = reverse_words(input_text)
    output_var.set(result)

def gui_save():
    text = output_var.get()
    if text:
        save_to_file(text)
    else:
        messagebox.showwarning("No Output", "Nothing to save. Please reverse some text first.")

def cli_main():
    print("=== Text Reverser ===")
    while True:
        print("\nMenu:")
        print("1. Reverse Character Order")
        print("2. Reverse Word Order")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '3':
            print("Goodbye!")
            break
        elif choice in ('1', '2'):
            text = input("Enter a sentence: ")
            if not text.strip():
                print("Error: Empty input. Please try again.")
                continue
            if choice == '1':
                result = reverse_characters(text)
                print(f"Reversed (characters): {result}")
            else:
                result = reverse_words(text)
                print(f"Reversed (words): {result}")
            save = input("Do you want to save the result to a file? (y/n): ").strip().lower()
            if save == 'y':
                try:
                    filename = input("Enter filename (e.g., output.txt): ").strip()
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(result)
                    print(f"Saved to {filename}")
                except Exception as e:
                    print(f"Error saving file: {e}")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def launch_gui():
    global entry, output_var
    root = tk.Tk()
    root.title("Text Reverser")

    tk.Label(root, text="Enter your text:").pack(pady=5)
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="Reverse Characters", command=lambda: gui_reverse("char")).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Reverse Words", command=lambda: gui_reverse("word")).pack(side=tk.LEFT, padx=5)

    output_var = tk.StringVar()
    tk.Label(root, text="Result:").pack(pady=5)
    output_entry = tk.Entry(root, textvariable=output_var, width=50, state='readonly')
    output_entry.pack(pady=5)

    tk.Button(root, text="Save Result to File", command=gui_save).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")
    mode = input("Enter 1 for CLI or 2 for GUI: ").strip()
    if mode == '2':
        launch_gui()
    else:
        cli_main()


# In[ ]:




