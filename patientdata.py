class Patient:
    def __init__(self, name, age, gender, email, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone
class Appointment:
    def __init__(self, patient, date, time):
        self.patient = patient
        self.date = date
        self.time = time
class AppointmentScheduler:
    def __init__(self):
        self.appointments = []
    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
    def get_daily_schedule(self, date):
        daily_schedule = [appt for appt in self.appointments if appt.date == date]
        return daily_schedule
if __name__=="__main__":
     schedul = AppointmentScheduler()
     patient1 = Patient("revan paul singh", 30, "Female", "revan27@gmail.com", "764-456-7060")
     patient2 = Patient("rajesh", 25, "Male", "rajeh2004@gmail.com", "942-482-8530")
     patient3 = Patient("mohanapriya",23,"Female","mohanapriya978@gmail.com","422-764-5647")
     patient4 = Patient("gayathri", 29, "female", "gayathri@gmail.com", "942-482-8530")
     appointment1 = Appointment(patient1, "2024-02-23", "11:00 AM")
     appointment2 = Appointment(patient2, "2024-02-23", "12:00 AM")
     appointment3 = Appointment(patient3, "2024-02-26", "04:00 AM")
     schedul.schedule_appointment(appointment1)
     schedul.schedule_appointment(appointment2)
     schedul.schedule_appointment(appointment3)
     schedule_date = "2024-02-23"
     daily_schedule = schedul.get_daily_schedule(schedule_date)
     print(f"Daily Schedule for {schedule_date}:")
     for app in daily_schedule:
         print(f"patient:{app.patient.name},time:{app.time}")
