class Patient():
    def __init__(self):
        print("Please enter all values regarding your patient:")
        self.male = int(input("Male [1/0]: "))
        self.age = int(input("Age: "))
        self.currrentSmoker = int(input("Current Smoker [1/0]: "))
        self.cigsPerDay = int(input("Amount of cigarettes per day: "))
        self.BPMeds = int(input("Is on blood pressure medications [1/0]:"))
        self.prevalentStroke = int(input("Does the patient had previously had a stroke [1/0]:"))
        self.prevalentHyp = int(input("Does the patient was hypertensive [1/0]:"))
        self.diabetes = int(input("Does the patient had diabetes [1/0]:"))
        self.totChol = int(input("Total Cholesterol level:"))
        self.sysBP = int(input("Systoloc blood pressure:"))
        self.diaBP = int(input("Diastolic blood pressure:"))
        self.BMI = int(input("Body Mass Index:"))
        self.heartRate = int(input("Heart rate:"))
        self.glucose = int(input("Glucose level:"))
    def to_array(self):
        return [self.male, self.age, self.currrentSmoker, self.cigsPerDay,
                self.BPMeds, self.prevalentStroke, self.prevalentHyp,
                self.diabetes, self.totChol, self.sysBP, self.diaBP,
                self.BMI, self.heartRate, self.glucose]