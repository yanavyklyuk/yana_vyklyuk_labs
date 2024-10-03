import datetime
from Entities.Doctor import Doctor
from Entities.Patient import Patient
from Entities.Specialization import Specialization
from Entities.Status import Status
from Entities.Favor import Favor

class Appointment:
    def __init__(self, id, datetime_of_appointment, doctor, patient, status, favor):
        if datetime_of_appointment <= datetime.datetime.now():
            raise ValueError("Appointment cannot be in the past")
        if not isinstance(patient, Patient):
            raise TypeError("Patient must be a patient object.")
        if not isinstance(doctor, Doctor):
            raise TypeError("Doctor must be a doctor object.")
        if not isinstance(status, Status):
            raise TypeError("Status must be a status object.")
        if not isinstance(favor, Favor):
            raise TypeError("Favor must be a favor object.")
        self.__id = id
        self.__datetime_of_appointment = datetime_of_appointment
        self.__doctor = doctor
        self.__patient = patient
        self.__status = status
        self.__favor = favor

    @property
    def id(self):
        return self.__id

    @property
    def datetime_of_appointment(self):
        return self.__datetime_of_appointment

    @property
    def doctor(self):
        return self.__doctor

    @property
    def patient(self):
        return self.__patient

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_name):
        if Status.is_valid_status_name(self.status, status_name):
            self.__status = Status(status_name)
        else:
            raise ValueError(f'Invalid status name: {status_name}')

    @property
    def favor(self):
        return self.__favor

    def __str__(self):
        return (f'Datetime of appointment: {self.__datetime_of_appointment}\nDoctor: {self.__doctor.first_name} {self.__doctor.last_name}\n'
                f'Patient: {self.__patient.first_name} {self.__patient.last_name}\nStatus: {self.__status.status_name}\nFavor: {self.__favor.favor_name}')