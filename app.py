# app.py

class Application:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running {self.name} application.")

    def get_status(self):
        return f"{self.name} is running smoothly."