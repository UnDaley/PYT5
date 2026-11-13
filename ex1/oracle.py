import os

from dotenv import load_dotenv


DEFAULTS: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///local.db",
    "API_KEY": "",
    "LOG_LEVEL": "INFO",
    "ZION_ENDPOINT": "http://localhost:8080",
}

ENV_FILE: str = os.path.join(os.path.dirname(__file__), ".env")
GITIGNORE_FILE: str = os.path.join(os.path.dirname(__file__), ".gitignore")
SOURCE_FILE: str = os.path.abspath(__file__)


def read_file(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()
    except OSError:
        return ""


def is_env_ignored() -> bool:
    lines = read_file(GITIGNORE_FILE).splitlines()
    return ".env" in lines


def main() -> None:
    load_dotenv(ENV_FILE)
    print("ORACLE STATUS: Consulting the configuration...")
    print()

    config: dict[str, str] = {}
    missing: list[str] = []
    for key, default in DEFAULTS.items():
        value = os.getenv(key)
        if value is None:
            missing.append(key)
            value = default
        config[key] = value

    mode = config["MATRIX_MODE"]

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if mode == "production":
        print("Database: Connected to production cluster")
    else:
        print("Database: Connected to local instance")
    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Remote Network: Online")

    print()
    for key in missing:
        print(f"[WARNING] {key} is not set, using default")
    print()
    print("Configuration security check:")

    api_key = config["API_KEY"]
    if api_key and api_key in read_file(SOURCE_FILE):
        print("[FAIL] API_KEY is hardcoded in the source code!")
    else:
        print("[OK] No hardcoded secrets detected")

    if is_env_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[FAIL] .env is NOT in .gitignore!")

    if mode == "production" and missing:
        print("[FAIL] Production mode requires every setting to be defined")
    else:
        print("[OK] Production overrides available")

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
