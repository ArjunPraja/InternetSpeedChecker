from tkinter import *
import speedtest


def speedcheck():
    try:
        sp = speedtest.Speedtest()
        download_speed = sp.download() / 1000000  # Convert to Mbps
        upload_speed = sp.upload() / 1000000  # Convert to Mbps

        down = f"{download_speed:.3f} Mbps"
        up = f"{upload_speed:.3f} Mbps"

        lab_down.config(text=down)
        lab_up.config(text=up)
        print("Speed Success Fully Checked")
    except Exception as e:
        error_message = "Error: " + str(e)
        print(error_message)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="black")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="black", fg="white")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Times New Roman", 30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=("Times New Roman", 30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=("Times New Roman", 30, "bold"), bg="red", relief=RAISED, command=speedcheck)
button.place(x=60, y=460, height=50, width=380)
sp.mainloop()
