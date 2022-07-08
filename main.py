import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

from tkinter.filedialog import askopenfile

#creating a window obj

root=tk.Tk() # start loop

canvas=tk.Canvas(root,width=600,height=300) #px
canvas.grid(columnspan=3) #initialise canvas in 3 invisible cols

logo= Image.open('PDFextract_text-main/starterFiles/logo.png')
logo= ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.grid(column=1,row=0)


#instructions
instructions=tk.Label(root,text="Select a PDF file on your computer to extract it's text")
instructions.grid(columnspan=3, column=0, row=1 )

#creating functionality for the browse button
def open_file():
    browse_text.set('Loading...')
    file= askopenfile(parent=root, mode='rb', title='Choose a file', filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf=PyPDF2.PdfFileReader(stream=file)
        page=read_pdf.getPage(0)
        page_content= page.extractText()
        #text box to display whatever page _content gives us
        text_box=tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center",justify="center")
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1,row=3)

        with open('rawtext.txt','w') as f:
            for line in page_content:
                f.write(line)


        browse_text.set("browse")



#browse button

browse_text=tk.StringVar() #will use to store text
browse_btn=tk.Button(root,textvariable=browse_text, command=lambda : open_file(), bg="#20bebe", fg="black", height=2, width=15)
browse_text.set("BROWSE")
browse_btn.grid(column=1,row=2)

canvas=tk.Canvas(root,width=600,height=300) #px
canvas.grid(columnspan=3) #initialise canvas in 3 invisible cols




root.mainloop() #end loop