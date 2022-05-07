import pygetwindow
from pygetwindow import Win32Window #so i can use typehint
from win10toast import ToastNotifier
import time

#edit this for other tabs
validWindowNames = {"iClicker","Question 1 Detail", "Question 2 Detail"}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    toaster = ToastNotifier()
    c:Win32Window = None
    while c is None:
        for s in validWindowNames:
            temp = pygetwindow.getWindowsWithTitle(s)
            if len(temp) > 0:
                c = temp[0]
                toaster.show_toast(title="Window Found", msg=f"Found a window with title {c.title}")
                break
        print("Did not find any windows")
        time.sleep(.5) #to prevent this process from running a ton

    # print(braveObama)
    previousTitle: str = c.title #why would you even have typehints just make the language static typing my god

    while True:
        if previousTitle != c.title:
            toaster.show_toast(title="PythonScript Notice",msg=f"Title changed from {previousTitle} to {c.title}.")
        #should this go before or after the sleep()
        previousTitle = c.title
        time.sleep(.5)

