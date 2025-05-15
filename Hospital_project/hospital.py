class Hospital:
    def __init__(self, doctor_name, docter_date, patient_name, patient_date):
        self.doctor = doctor_name
        self.doctor_date = docter_date
        self.patient = patient_name
        self.patient_date = patient_date
        self.doctors = [self.doctor]
        self.patients = [self.patient]
    
    def add_new_doctor(self, new_doctor):
        return self.doctors.append(new_doctor)
    
    def resgin_doctor(self, resign_doctor):
        if resign_doctor in self.doctors:
            return self.doctors.remove(resign_doctor)
        else:
            return "doctor not found !"
        
    def add_new_patient(self, new_patient):
        return self.patients.append(new_patient)
    
    def patient_fine(self, fine_patient):
        if fine_patient in self.patients:
            return self.patients.remove(fine_patient)
        else:
            "patient not found !"

hos1 = Hospital("dr salman", "10/3/2020", "patient 002", "8/1/2024")
print(hos1.doctors)
print(hos1.patient)
hos1.add_new_doctor("dr pk")
hos1.add_new_patient("patient 0091")
print(hos1.doctors)
print(hos1.patients)
hos1.resgin_doctor("dr pk")
hos1.patient_fine("patient 002")
print(hos1.doctors)
print(hos1.patients)