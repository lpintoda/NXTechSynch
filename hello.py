"""
NX Tech Synch - My First Python Script
A simple demo script to showcase Git push/pull workflows.
"""

import platform
from datetime import datetime


def greet(name):
    return f"Hello, {name}! Welcome to the NX Tech Synch session."


def system_info():
    return {
        "python_version": platform.python_version(),
        "os": platform.system(),
        "machine": platform.machine(),
    }


def main():
    print("=" * 50)
    print("  NX Tech Synch - Python & Git Demo")
    print("=" * 50)

    name = input("\nWhat's your name? ")
    print(f"\n{greet(name)}")

    print(f"\nCurrent date/time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    info = system_info()
    print("\nSystem Info:")
    for key, value in info.items():
        print(f"  {key}: {value}")

    print("\nScript ran successfully! 🎉")


if __name__ == "__main__":
    main()
