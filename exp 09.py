# Simple Hospital Management System

class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease

    def show(self):
        print("ID:", self.pid, "| Name:", self.name,
              "| Age:", self.age, "| Disease:", self.disease)


class Doctor:
    def __init__(self, did, name, specialization):
        self.did = did
        self.name = name
        self.specialization = specialization

    def show(self):
        print("ID:", self.did, "| Name:", self.name,
              "| Specialization:", self.specialization)


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = [] # list to store patients
        self.doctors = [] # list to store doctors

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully!")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print("Doctor added successfully!")

    def show_patients(self):
        print("\n--- Patient List ---")
        if len(self.patients) == 0:
            print("No patients found.")
        for p in self.patients:
            p.show()

    def show_doctors(self):
        print("\n--- Doctor List ---")
        if len(self.doctors) == 0:
            print("No doctors found.")
        for d in self.doctors:
            d.show()

    def search_patient(self, pid):
        for p in self.patients:
            if p.pid == pid:
                print("Patient found:")
                p.show()
                return
        print("Patient not found.")


# ---------- Main Program ----------
hospital = Hospital("City Care Hospital")

while True:
    print("\n===", hospital.name, "===")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Show Patients")
    print("4. Show Doctors")
    print("5. Search Patient by ID")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = int(input("Enter patient ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        disease = input("Enter disease: ")
        p = Patient(pid, name, age, disease)
        hospital.add_patient(p)

    elif choice == "2":
        did = int(input("Enter doctor ID: "))
        name = input("Enter name: ")
        spec = input("Enter specialization: ")
        d = Doctor(did, name, spec)
        hospital.add_doctor(d)

    elif choice == "3":
        hospital.show_patients()

    elif choice == "4":
        hospital.show_doctors()

    elif choice == "5":
        pid = int(input("Enter patient ID to search: "))
        hospital.search_patient(pid)

    elif choice == "6":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice, try again.")