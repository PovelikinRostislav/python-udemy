from mypackage.foo_module import print_foo

print(f"__name__ IS {__name__}")
print(f"__package__ IS {__package__}")
if '__path__' in globals():
    print(f"__path__ IS {__path__}")
print("----")

print_foo()

import mypackage
print(f"mypackage.__path__  IS {mypackage.__path__}")
print(f"mypackage.__package__ IS {mypackage.__package__}")
print("----")

import mypackage.subpkg as subpkg
print(f"subpkg.__path__ IS {subpkg.__path__}")
print(f"subpkg.__package__ IS {subpkg.__package__}")
print("----")

import mypackage.subpkg.bar_module

print(mypackage.__spec__)
print("----")
