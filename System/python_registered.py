import sys

from _winreg import *

# tweak as necessary
version = sys.version[:3]
installpath = sys.prefix

regpath = "SOFTWARE\\Python\\Pythoncore\\%s\\" % (version)
installkey = "InstallPath"
pythonkey = "PythonPath"
pythonpath = "%s;%s\\Lib\\;%s\\DLLs\\" % (
  installpath, installpath, installpath
)

def RegisterPy():
  try:
    reg = OpenKey(HKEY_CURRENT_USER, regpath)
  except EnvironmentError as e:
    try:
      reg = CreateKey(HKEY_CURRENT_USER, regpath)
      SetValue(reg, installkey, REG_SZ, installpath)
      SetValue(reg, pythonkey, REG_SZ, pythonpath)
      CloseKey(reg)
    except:
      print "*** Unable to register!"
      return
    print "--- Python", version, "is now registered!"
    return
  if (QueryValue(reg, installkey) == installpath and
    QueryValue(reg, pythonkey) == pythonpath):
    CloseKey(reg)
    print "=== Python", version, "is already registered!"
    return
  CloseKey(reg)
  print "*** Unable to register!"
  print "*** You probably have another Python installation!"

if __name__ == "__main__":
  RegisterPy()
