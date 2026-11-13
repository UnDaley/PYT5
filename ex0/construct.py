import sys
import os
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def show_outside() -> None:
    print("LABORATORY STATUS: You are working in the open")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print(r"lab_env\Scripts\activate # On Windows")
    print()
    print("Then run this program again.")


def get_site_packages() -> str:
    paths = site.getsitepackages()
    for path in paths:
        if path.endswith("site-packages"):
            return path
    return paths[0]


def show_inside() -> None:
    print("LABORATORY STATUS: The laboratory is sealed")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.")
    print()
    print("Reagent installation path:")
    print(get_site_packages())


def main() -> None:
    if is_in_venv():
        show_inside()
    else:
        show_outside()


if __name__ == "__main__":
    main()
