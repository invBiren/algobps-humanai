from importlib import import_module

# Run this from the parent directory that contains `backend` so the import works.
# Example:
# Set-Location 'C:\algobps-humanai'
# python print_routes.py

app = import_module('backend.main').app

for route in app.routes:
    methods = getattr(route, 'methods', None)
    print(route.path, methods)
