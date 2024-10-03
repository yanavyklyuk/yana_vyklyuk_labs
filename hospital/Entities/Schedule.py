import datetime
from Entities.Doctor import Doctor
from Entities.Specialization import Specialization
class Schedule:
    def __init__(self, id, start_of_work, end_of_work, time_per_patient, cabinet_number, doctor):
        if not isinstance(start_of_work, datetime.datetime):
            raise TypeError("Start of work must be a datetime.time object.")
        if not isinstance(end_of_work, datetime.datetime):
            raise TypeError("End of work must be a datetime.time object.")
        if start_of_work >= end_of_work:
            raise ValueError("Start of work must be before end of work.")
        if time_per_patient <= 0:
            raise ValueError("Time per patient must be greater than 0.")
        if not isinstance(cabinet_number, int) or cabinet_number <= 0:
            raise ValueError("Cabinet number must be a positive integer.")
        if not isinstance(doctor, Doctor):
            raise TypeError("Doctor must be a doctor object.")
        self.__id = id
        self.__start_of_work = start_of_work
        self.__end_of_work = end_of_work
        self.__time_per_patient = time_per_patient
        self.__cabinet_number = cabinet_number
        self.__doctor = doctor
        self.appointment_slots = self.generate_slots()

    @property
    def id(self):
        return self.__id

    @property
    def start_of_work(self):
        return self.__start_of_work

    @property
    def end_of_work(self):
        return self.__end_of_work

    @property
    def time_per_patient(self):
        return self.__time_per_patient

    @property
    def cabinet_number(self):
        return self.__cabinet_number

    @property
    def doctor(self):
        return self.__doctor

    def __str__(self):
        return(f'Doctor: {self.doctor.first_name} {self.doctor.last_name}\n'
                f'Start of Work: {self.start_of_work}\n'
                f'End of Work: {self.end_of_work}\n'
                f'Time per Patient: {self.time_per_patient} minutes\n'
                f'Cabinet Number: {self.cabinet_number}')

    def generate_slots(self):
        slots = {}
        current_time = self.__start_of_work

        while current_time < self.__end_of_work:
            slots[current_time] = True
            current_time += datetime.timedelta(minutes=self.time_per_patient)

        return slots

    def is_slot_available(self, start_time):
        return self.appointment_slots.get(start_time) is True