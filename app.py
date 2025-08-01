class Application:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running {self.name} application.")

    def get_status(self):
        return f"{self.name} is running smoothly."

    def install_package(self, package_name):
        print(f"Installing {package_name} using {self.name}.")

# Initial comment for commit 1