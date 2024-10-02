from Entities.Appointment import Appointment
class AppointmentList:
    def __init__(self):
        self.appointments = []

    @staticmethod
    def is_appointment(appointment):
        if not isinstance(appointment, Appointment):
            raise TypeError("Appointment must be an appointment object.")
        return True

    def add_appointment(self, appointment):
        if self.is_appointment(appointment):
            self.appointments.append(appointment)

    def remove_appointment(self, appointment):
        if self.is_appointment(appointment) and appointment in self.appointments:
            self.appointments.remove(appointment)
            return f"Appointment has been removed."
        else:
            return f"Appointment not found in the list."

    def get_appointment_by_id(self, id):
        for appointment in self.appointments:
            if appointment.id == id:
                return appointment
        return None