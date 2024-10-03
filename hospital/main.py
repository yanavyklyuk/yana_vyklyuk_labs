import datetime
from Entities.Doctor import Doctor
from Entities.Patient import Patient
from Entities.Appointment import Appointment
from Entities.Human import Human
from Entities.Specialization import Specialization
from Entities.Status import Status
from Entities.Disease import Disease
from Entities.DiseaseHistory import DiseaseHistory
from Entities.Favor import Favor
from Entities.Schedule import Schedule
from Repository.AppointmentList import AppointmentList
from Repository.DoctorList import DoctorList
from Repository.PatientList import PatientList

def main():
    doctor_list = DoctorList()
    patient_list = PatientList()
    appointment_list = AppointmentList()

    person = Human(0, 'Ada', 'Li','female', datetime.date(2002,11,1),
                   '9302393')
    specialization1 = Specialization(1, 'Cardiologist')
    date_of_birth_d1 = datetime.date(2000, 10, 11)
    doctor1 = Doctor(1,'Kim', 'Bim','female', date_of_birth_d1, '9302392',
                     specialization1, 1)

    date_of_birth_p1 = datetime.date(1999, 12, 13)
    patient1 = Patient(2,'John', 'Watson','male', date_of_birth_p1, '9302392',
                     'Ukraine', 'Lviv', 'Bandera 2')

    print(f'Greeting of human: {person.greet()}')
    print('Polymorphism')
    print(f'Greeting of doctor: {doctor1.greet()}')
    print(f'Greeting of patient: {patient1.greet()}\n')
    print('Method of doctor:')
    print(doctor1.treat() + '\n')
    print('Method of patient:')
    print(patient1.sicken() + '\n')

    doctor1.last_name = 'Black'
    print(doctor1)
    print(f'The ID of the doctor: {doctor1.id}\n')

    specialization2 = Specialization(2, 'Dentist')
    doctor2 = Doctor(id=3, first_name='John', last_name='Doe', sex='male',
                     date_of_birth=datetime.date(1970, 10, 2), phone_number='123456789',
                     specialization=specialization2, experience=10)
    patient2 = Patient(id=4, first_name='Jane', last_name='Smith', sex='female',
                       date_of_birth=datetime.date(1980, 2, 2), phone_number='987654321',
                       country='USA', city='New York', street='5th Avenue')
    service1 = Favor(favor_name='Consultation', cost=100)
    status1 = Status('scheduled')

    appointment = Appointment(1,datetime.datetime(2025, 2, 2, 9, 0),doctor2, patient2,
                              status1, service1)
    appointment_list.add_appointment(appointment)
    print(f'Appointment:\n{appointment}\n')
    appointment.status = 'CANCELLED'
    print(f'Appointment after status change:\n{appointment}\n')

    schedule1 = Schedule(id=1, start_of_work=datetime.datetime(2024, 10, 1,9,0),
                        end_of_work=datetime.datetime(2024, 10, 1,17,0),
                        time_per_patient=30, cabinet_number=101, doctor=doctor1)
    print(f'Slots for patients: {schedule1.generate_slots()}\n')
    print(f'Schedule:\n{schedule1}\n')

    disease = Disease(id=1, disease_name='Hypertension')
    disease_history = DiseaseHistory(id=1, disease_duration=30, patient=patient1,
                                     doctor=doctor1, disease=disease)
    print(f'Disease history:\n{disease_history}\n')

    doctor_list.add_doctor(doctor1)
    doctor_list.add_doctor(doctor2)
    print(doctor_list, '\n')
    doctor_list.remove_doctor(doctor1)
    print('After remove of doctor')
    print(doctor_list, '\n')

    patient_list.add_patient(patient1)
    patient_list.add_patient(patient2)
    print(patient_list, '\n')
    patient_list.remove_patient(patient2)
    print('After remove of doctor')
    print(patient_list, '\n')

    print(doctor_list.get_doctor_by_id(doctor1.id))
    print(doctor_list.get_doctor_by_id(doctor2.id),  '\n')

    print(patient_list.get_patient_by_id(patient1.id))
    print(patient_list.get_patient_by_id(patient2.id))

    appointment_list.add_appointment(appointment)

if __name__ == "__main__":
    main()
