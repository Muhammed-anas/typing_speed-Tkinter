#----------------------IMPORT-----------------------#
from tkinter import *
from words_list import words

#----------------------BG COLOR AND FONTS-----------------------#
Bg = "#7be1bf"
canvas_bg = "#CCCCFF"
font = ("Ariel", 30)

#----------------------SET WINDOW-----------------------#
window = Tk()
window.title("Typing speed Checker")
window.geometry("700x500")
window.config(padx=100, pady=50, bg=Bg)

#----------------------WORD COUNT-----------------------#
words_count = -1
how_much_words = 0


#----------------------DISPLAY THE WORDS FROM WORDS_LIST FILE-----------------------#
def display_words():
    global words_count, current_word
    words_count += 1
    current_word = words[words_count]
    canvas.itemconfig(flash_word, text=current_word, fill="white")


#----------------------CALL THE ENTRY FUNCTION-----------------------#
def func(event=None):
    global how_much_words, current_word
    user_input = user_entry.get()
    if user_input == current_word:
        user_entry.delete(0, END)
        how_much_words += 1

    else:
        user_entry.delete(0, END)
    display_words()


#----------------------SET ONE MINUTE-----------------------#
def one_minute():
    window.after(60000, end_program)


#----------------------END PROGRAM AFTER ONE MINUTE-----------------------#
def end_program():
    user_entry.config(state="disabled")
    canvas.itemconfig(flash_word, text=f"You typed {how_much_words}/WPM ", fill="blue")
    print(f"You typed {how_much_words}/WPM")
    print(f"You typed {(words_count - how_much_words)} wrongly")


#----------------------SET THE CANVAS-----------------------#
canvas = Canvas()
canvas.config(width=500, height=300, bg=canvas_bg)
canvas.grid(column=0, row=1)
flash_word = canvas.create_text(240, 120, font=("Ariel", 25, 'bold'))


#----------------------LABEL,ENTRY -----------------------#
head_label = Label(text="Typing speed checker", bg=Bg, font=font, pady=20)
head_label.grid(column=0, row=0)

user_entry = Entry(width=20, highlightthickness=0, font=("Ariel", 15))
user_entry.place(x=130, y=270, height=40)

#----------------------USE BIND FUNCTION TO RETURN THE ENTRY OUTPUT -----------------------#
user_entry.bind("<Return>", func)

#----------------------DISPLAY -----------------------#
display_words()
one_minute()

#----------------------RUN THE LOOP UNTIL CLOSE THE WINDOW -----------------------#
window.mainloop()
