import win32clipboard as w
import win32con
import win32api


def getText():  # 读取剪切板
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d.decode('utf-8')


def setText(aString):  # 写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

setText('tom,lalala')
st = getText()
print(st)
win32api.MessageBox(None,st,'dong',win32con.MB_OK)