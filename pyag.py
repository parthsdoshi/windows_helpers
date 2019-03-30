import pyautogui
pyautogui.FAILSAFE = True
import time

import pythoncom
import pyWinhook
import win32gui
import win32com.client as client

sa = client.Dispatch('Shell.Application')
print(sa)
print(sa.Windows().count)
for window in sa.Windows():
    print(window.FullName)
    print(window.LocationURL)
    print(window.document.folder.self.path)

exit()
time.sleep(3)


# print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))

# should be '#32770'
print(win32gui.GetClassName(win32gui.GetForegroundWindow()))
w = win32gui.GetForegroundWindow()
def p_w(hwnd, param):
    print(win32gui.GetWindowText(hwnd), win32gui.GetClassName(hwnd))
    if win32gui.GetClassName(hwnd) == "Edit":
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SetFocus(hwnd)

    # print(win32gui.GetClassName(hwnd))
    return True

win32gui.EnumChildWindows(w, p_w, None)
exit()

# time.sleep(3)
# pyautogui.hotkey('alt', 'd')
# pyautogui.typewrite('C:\\Users\\ParthSanjivDoshi\\')
# pyautogui.press('enter')
# pyautogui.typewrite(['tab'] * 5)
# pyautogui.password('Enter password (text will be hidden)')

def OnKeyboardEvent(event):
    print('MessageName: %s' % event.MessageName)
    print('Message: %s' % event.Message)
    print('Time: %s' % event.Time)
    print('Window: %s' % event.Window)
    print('WindowName: %s' % event.WindowName)
    print('Ascii: %s' %  event.Ascii, chr(event.Ascii))
    print('Key: %s' %  event.Key)
    print('KeyID: %s' %  event.KeyID)
    print('ScanCode: %s' %  event.ScanCode)
    print('Extended: %s' %  event.Extended)
    print('Injected: %s' %  event.Injected)
    print('Alt %s' %  event.Alt)
    print('Transition %s' %  event.Transition)

    return True

# create a hook manager
hm = pyWinhook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()