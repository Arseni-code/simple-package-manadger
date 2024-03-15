import os
import shutil
import sys

PACKAGES_DIR = "/home/arseni/a!package_manager/packages"  # Путь к директории с пакетами
INSTALLATION_DIR = "/home/arseni/a!package_manager/package_placement"  # Путь к директории для установки пакетов

def install(package_name):
    package_path = os.path.join(PACKAGES_DIR, package_name)
    if os.path.exists(package_path):
        try:
            shutil.copytree(package_path, os.path.join(INSTALLATION_DIR, package_name))
            print(f"Package '{package_name}' has installed successfully!")
        except FileExistsError:
            print(f"Package '{package_name}' has already installed!")
        except Exception as e:
            print(f"Failed to install package '{package_name}': {str(e)}")
    else:
        print(f"Package '{package_name}' does not exist.")

def uninstall(package_name):
    package_path = os.path.join(INSTALLATION_DIR, package_name)
    if os.path.exists(package_path):
        try:
            shutil.rmtree(package_path)
            print(f"Package '{package_name}' has uninstalled successfully!")
        except Exception as e:
            print(f"Failed to uninstall package '{package_name}': {str(e)}")
    else:
        print(f"Package '{package_name}' is not installed.")

def list_installed_packages():
    packages = [name for name in os.listdir(INSTALLATION_DIR) if os.path.isdir(os.path.join(INSTALLATION_DIR, name))]
    print("Installed packages:")
    for package in packages:
        print(package)

# Обработка команд из командной строки
if __name__ == "__main__":
    command = input()
    command = command.split()

    if command[0] == "install":
        install(command[1])
    elif command[0] == "uninstall":
        uninstall(command[1])
    elif command[0] == "list_installed_packages":
        list_installed_packages()
    elif command[0] == "help":
        print("Usage:")
        print("- To install a package: python package_manager.py install <package_name>")
        print("- To uninstall a package: python package_manager.py uninstall <package_name>")
        print("- To list installed packages: python package_manager.py list")
