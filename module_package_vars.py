print(f"__name__ IS {__name__}")
print(f"__package__ IS {__package__}")
if '__path__' in globals():
    print(f"__path__ IS {__path__}")
print("----")

import mypackage.foo_module

import mypackage
print(f"mypackage.__path__  IS {mypackage.__path__}")
print(f"mypackage.__package__ IS {mypackage.__package__}")
print(f"mypackage.__spec__ IS {mypackage.__spec__}")
print("----")

import mypackage.subpkg as subpkg
print(f"subpkg.__path__ IS {subpkg.__path__}")
print(f"subpkg.__package__ IS {subpkg.__package__}")
print("----")

import mypackage.subpkg.bar_module
