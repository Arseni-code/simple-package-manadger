import os
import shutil
import sys

PACKAGES_DIR = "/home/user/packages"  # Путь к директории с пакетами
INSTALLATION_DIR = "/home/user/package_manager"  # Путь к директории для установки пакетов

def install(package_name):
    package_path = os.path.join(PACKAGES_DIR, package_name)
    if os.path.exists(package_path):
        try:
            shutil.copytree(package_path, os.path.join(INSTALLATION_DIR, package_name))
            print(f"Package '{package_name}' has been installed successfully!")
        except Exception as e:
            print(f"Failed to install package '{package_name}': {str(e)}")
    else:
        print(f"Package '{package_name}' does not exist.")

def uninstall(package_name):
    package_path = os.path.join(INSTALLATION_DIR, package_name)
    if os.path.exists(package_path):
        try:
            shutil.rmtree(package_path)
            print(f"Package '{package_name}' has been uninstalled successfully!")
        except Exception as e:
            print(f"Failed to uninstall package '{package_name}': {str(e)}")
    else:
        print(f"Package '{package_name}' is not installed.")

def list_installed_packages():
    packages = [name for name in os.listdir(INSTALLATION_DIR) if os.path.isdir(os.path.join(INSTALLATION_DIR, name))]
    print("Installed packages:")
    for package in packages:
        print(f"- {package}")

# Обработка команд из командной строки
if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else None
    package_name = sys.argv[2] if len(sys.argv) > 2 else None

    if command == "install" and package_name:
        install(package_name)
    elif command == "uninstall" and package_name:
        uninstall(package_name)
    elif command == "list":
        list_installed_packages()
    else:
        print("Usage:")
        print("- To install a package: python package_manager.py install <package_name>")
        print("- To uninstall a package: python package_manager.py uninstall <package_name>")
        print("- To list installed packages: python package_manager.py list")

