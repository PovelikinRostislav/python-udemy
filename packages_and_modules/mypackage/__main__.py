print("I'm MAIN of the mypackage")
print(f"__name__ IS {__name__}")
print(f"__package__ IS {__package__}")
if '__path__' in globals():
    print(f"__path__ IS {__path__}")
print("----")
