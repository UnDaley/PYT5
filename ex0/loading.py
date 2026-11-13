import importlib


REAGENTS: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}


def get_version(name: str) -> str | None:
    try:
        module = importlib.import_module(name)
    except ImportError:
        return None
    return str(module.__version__)


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    missing: list[str] = []
    for name, description in REAGENTS.items():

        version = get_version(name)
        if version is None:

            print(f"[MISSING] {name} - not installed")
            missing.append(name)
        else:
            print(f"[OK] {name} ({version}) - {description}")
    print()
    print("pip vs Poetry:")
    print("  requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, and Poetry pins "
          "the resolved")
    print("  versions in poetry.lock so every install is identical.")
    print()
    if missing:
        print("Missing reagents! Install them with:")
        print("  pip:    pip install -r ex0/requirements.txt")
        print("  Poetry: poetry -C ex0 install")
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
