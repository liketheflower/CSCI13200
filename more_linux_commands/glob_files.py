import glob

files = glob.glob("./*.py")
print(files)
files = glob.glob("./*[0-9].py")
print(files)
