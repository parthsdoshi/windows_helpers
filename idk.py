import pyWinhook
import pythoncom

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

    if chr(event.Ascii) == 'a':
        return False

    return True

# create a hook manager
hm = pyWinhook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()