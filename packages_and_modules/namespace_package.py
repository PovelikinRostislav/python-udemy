import sys

sys.path.append('./package_one')
sys.path.append('./package_two')
import parent

print("----")
print("'parent' package is located as two different directories under 'package_one' and 'package_two'")
print("it's __path__ contains both of those paths cause it's a namespace package and it doesn't require subpackages to reside in the same filesystem place")
print("Also we can see this in submodule_search_locations of module's spec:")
print(f"__path__ of parent package: {parent.__path__}")
print(f"__spec__ of parent package: {parent.__spec__}")

print("----")
print("Namespace packages are useful ONLY for the cases when different libraries contibute to the same package")
print("Otherwise, use __init__.py files to indicate regular packages. If you are not following this, many built-in tools will fail")
print("E.g. unittest won't search subdirs w/o __init__.py cause it's not regular package")
