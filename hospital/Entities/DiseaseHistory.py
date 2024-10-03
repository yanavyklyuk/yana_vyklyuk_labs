from Entities.Patient import Patient
from Entities.Doctor import Doctor
from Entities.Disease import Disease
class DiseaseHistory:
    def __init__(self, id, disease_duration, patient, doctor, disease):
        if disease_duration <= 0:
            raise ValueError("Disease duration must be greater than 0.")
        if not isinstance(patient, Patient):
            raise TypeError("Patient must be a patient object.")
        if not isinstance(doctor, Doctor):
            raise TypeError("Doctor must be a doctor object.")
        if not isinstance(disease, Disease):
            raise TypeError("Disease must be a disease object.")
        self.__id = id
        self.__disease_duration = disease_duration
        self.__patient = patient
        self.__doctor = doctor
        self.__disease = disease

    @property
    def id(self):
        return self.__id

    @property
    def disease_duration(self):
        return self.__disease_duration

    @property
    def patient(self):
        return self.__patient

    @property
    def doctor(self):
        return self.__doctor

    @property
    def disease(self):
        return self.__disease

    def __str__(self):
        return (f'Patient: {self.__patient.first_name} {self.__patient.last_name}\n'
                f'Doctor: {self.__doctor.first_name} {self.__doctor.last_name}\n'
                f'Disease: {self.__disease.disease_name}\n'
                f'Disease Duration: {self.__disease_duration} days')