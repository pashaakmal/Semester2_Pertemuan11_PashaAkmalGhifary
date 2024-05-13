class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc,'')
    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                svc, "message you pay $",
                Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc,'')
    def list_pricing(self, services):
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                svc, "pesan Anda membayar $",
                Model.services[svc]['price'])

class Controller(object):
    def __init__(self, language):
        self.model = Model()
        if language == "1":
            self.view = View()
        elif language == "2":
            self.view = View2()
        else:
            print("Error, choose the language number!")

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)


# Instansiasi objek controller dengan pilihan bahasa
language_choice = (input("What language do you choose? [1]English [2]Indonesia: "))
controller = Controller(language_choice) 
if language_choice == "1":
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()
    
elif language_choice == "2":
    print("Layanan yang Tersedia:")
    controller.get_services()
    print("Harga untuk Layanan:")
    controller.get_pricing()

else :
    print("Error, choose the language number!")