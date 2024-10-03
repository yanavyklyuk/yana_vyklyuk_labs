import datetime
from Entities.Doctor import Doctor
from Entities.Specialization import Specialization

class DoctorList:
    def __init__(self):
        self.doctors = []

    @staticmethod
    def is_doctor(doctor):
        if not isinstance(doctor, Doctor):
            raise TypeError("Doctor must be a doctor object.")
        return True

    def add_doctor(self, doctor):
        if self.is_doctor(doctor):
            self.doctors.append(doctor)

    def remove_doctor(self, doctor):
        if self.is_doctor(doctor) and doctor in self.doctors:
            self.doctors.remove(doctor)
            return f"Doctor {doctor.first_name} {doctor.last_name} has been removed."
        else:
            return f"Doctor {doctor.first_name} {doctor.last_name} not found in the list."

    def get_doctor_by_id(self, id):
        for doctor in self.doctors:
            if doctor.id == id:
                return doctor
        return None

    def __str__(self):
        return 'Doctors: ' + ', '.join(f'{doctor.first_name} {doctor.last_name}' for doctor in self.doctors)

doctor1 = Doctor(1,'Kim', 'Sinn','male', datetime.date(2022, 10, 11),
                 '9302392', Specialization(1,'Therapist'), 9)