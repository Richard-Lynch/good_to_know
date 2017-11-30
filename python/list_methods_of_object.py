#!/usr/local/bin/python3
# sub the name of the object for the word object below
methods = [method_name for method_name in dir(object) if callable(getattr(object, method_name))]
