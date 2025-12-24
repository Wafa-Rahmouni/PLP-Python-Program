class Device:
    """Base class for electronic devices"""
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_on = False
    
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON")
        else:
            print(f"{self.brand} {self.model} is already ON")
    
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF")
        else:
            print(f"{self.brand} {self.model} is already OFF")
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Battery level: {self.battery_level}%")
    
    def use_battery(self, amount):
        if self.battery_level >= amount:
            self.battery_level -= amount
            return True
        else:
            print("Low battery!")
            return False

class Smartphone(Device):
    """Smartphone class inheriting from Device"""
    def __init__(self, brand, model, storage_gb, battery_level=100):
        super().__init__(brand, model, battery_level)
        self.storage_gb = storage_gb
        self.apps_installed = []
        self.current_app = None
    
    def install_app(self, app_name, app_size_gb):
        if self.storage_gb >= app_size_gb:
            self.apps_installed.append(app_name)
            self.storage_gb -= app_size_gb
            print(f"Installed {app_name}. Storage remaining: {self.storage_gb}GB")
        else:
            print(f"Not enough storage to install {app_name}")
    
    def open_app(self, app_name):
        if app_name in self.apps_installed:
            if self.use_battery(2):
                self.current_app = app_name
                print(f"Opened {app_name}")
            else:
                print("Cannot open app - battery too low")
        else:
            print(f"{app_name} is not installed")
    
    def make_call(self, phone_number):
        if self.use_battery(5):
            print(f"Calling {phone_number}...")
        else:
            print("Cannot make call - battery too low")
    
    def take_photo(self):
        if self.use_battery(3):
            print("Photo taken!")
        else:
            print("Cannot take photo - battery too low")
    
    def get_status(self):
        status = f"{self.brand} {self.model}\n"
        status += f"Battery: {self.battery_level}%\n"
        status += f"Storage: {self.storage_gb}GB\n"
        status += f"Apps: {len(self.apps_installed)}\n"
        status += f"Current app: {self.current_app or 'None'}\n"
        status += f"Power: {'ON' if self.is_on else 'OFF'}"
        return status

def demonstrate_smartphone():
    
    # Create smartphone objects
    phone1 = Smartphone("Apple", "iPhone 15", 128)
    phone2 = Smartphone("Samsung", "Galaxy S24", 256)
    
    # Demonstrate functionality
    phone1.turn_on()
    phone1.install_app("WhatsApp", 2)
    phone1.install_app("Instagram", 3)
    phone1.open_app("WhatsApp")
    phone1.take_photo()
    phone1.make_call("123-456-7890")
    
    print("\n" + phone1.get_status())
    
    phone2.turn_on()
    phone2.charge(20)
    phone2.install_app("TikTok", 4)
    
    print("\n" + phone2.get_status())

if __name__ == "__main__":
    demonstrate_smartphone()
