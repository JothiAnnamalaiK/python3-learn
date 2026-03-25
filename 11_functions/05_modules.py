# List of built-in modules: https://docs.python.org/3/py-modindex.html

import math  # built-in modules

import modules.mymodules_05 as mymod  # custom module

import requests  # external module


print("math sqrt: ", math.sqrt(4))

print("custom greet: ", mymod.greet("Jothi Annamalai"))


# external library

response = requests.get("https://google.com")
print("Google response : ", response.status_code)
