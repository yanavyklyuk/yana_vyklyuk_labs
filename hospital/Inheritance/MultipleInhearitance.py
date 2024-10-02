class Doctor:
    def __init__(self, worker_id, first_name, last_name, specialization):
        self.worker_id = worker_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization

    def get_doctor_info(self):
        return f"ID: {self.worker_id}, Name: {self.first_name} {self.last_name}, Specialization: {self.specialization}"

    def greet_doctor(self):
         print(f"I'm doctor {self.first_name} {self.last_name}")


class LabTechnician:
    def __init__(self, worker_id, first_name, last_name, lab_id):
        self.worker_id = worker_id
        self.first_name = first_name
        self.last_name = last_name
        self.lab_id = lab_id

    def get_lab_technician_info(self):
        return f"ID: {self.worker_id}, Name: {self.first_name} {self.last_name}, Lab ID: {self.lab_id}"

    def greet_lab_technician(self):
         print(f"I'm lab technician {self.first_name} {self.last_name}")


class Intern(Doctor, LabTechnician):
    def __init__(self, worker_id, first_name, last_name, specialization, lab_id):
        Doctor.__init__(self, worker_id, first_name, last_name, specialization)
        LabTechnician.__init__(self, worker_id, first_name, last_name, lab_id)

    def get_intern_info(self):
        return (f"ID: {self.worker_id}, Name: {self.first_name} {self.last_name}, "
                f"Specialization: {self.specialization}, Lab ID: {self.lab_id}")


doctor = Doctor(1, "John", "Doe", "Cardiology")
lab_technician = LabTechnician(2, "Jane", "Smith", "Lab_101")
intern = Intern(3, "Alice", "Johnson", "Pediatrics", "Lab_102")

print(doctor.get_doctor_info())
print(lab_technician.get_lab_technician_info())
print(intern.get_intern_info() + '\n')

intern.greet_doctor()
intern.greet_lab_technician()