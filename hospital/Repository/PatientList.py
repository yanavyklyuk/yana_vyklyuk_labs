from Entities.Patient import Patient

class PatientList:
    def __init__(self):
        self.patients = []

    @staticmethod
    def is_patient(patient):
        if not isinstance(patient, Patient):
            raise TypeError("Patient must be a patient object.")
        return True

    def add_patient(self, patient):
        if self.is_patient(patient):
            self.patients.append(patient)

    def remove_patient(self, patient):
        if self.is_patient(patient) and patient in self.patients:
            self.patients.remove(patient)
            return f"Patient {patient.first_name} {patient.last_name} has been removed."
        else:
            return f"Patient {patient.first_name} {patient.last_name} not found in the list."

    def get_patient_by_id(self, id):
        for patient in self.patients:
            if patient.id == id:
                return patient
        return None

    def __str__(self):
        return 'Patients: ' + ', '.join(f'{patient.first_name} {patient.last_name}' for patient in self.patients)