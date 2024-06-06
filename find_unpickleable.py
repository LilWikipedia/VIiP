import os
import pickle
import importlib.util
import inspect

def is_pickleable(obj):
    try:
        pickle.dumps(obj)
        return True
    except pickle.PicklingError:
        return False
    except AttributeError:
        return False

def get_unpickleable_functions(file_path):
    unpickleable = []
    try:
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name, func in inspect.getmembers(module, inspect.isfunction):
            if not is_pickleable(func):
                unpickleable.append(name)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    return unpickleable

repo_path = os.getcwd()

for root, _, files in os.walk(repo_path):
    for file in files:
        if file.endswith('.py') and file != 'find_unpickleable.py':  # Skip the script file itself
            file_path = os.path.join(root, file)
            unpickleable_functions = get_unpickleable_functions(file_path)
            if unpickleable_functions:
                print(f"Unpickleable functions in {file_path}: {unpickleable_functions}")

