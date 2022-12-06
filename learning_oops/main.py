import datetime as dt
import random

legs = ["Left Leg", "Right Leg"]
arms = ["Left Arm", "Right Arm"]
head = {
    "eyes": 2,
    "noses": 1,
    "mouths": 1,
    "ears": 2
}

main_body = ["Bones", "Skin", "Organs"]
available_sex_types = ["Male", "Female"]
all_body_parts = [legs, head]


class Human:
    sex = random.choice(available_sex_types)
    body = [all_body_parts]

    def __init__(self):
        date_now = dt.date.today()
        self.born_date = f"{date_now.year}{date_now.month}{date_now.day}"
        self.user_name = self.choose_name()
        self.id_code = self.make_id()

    def choose_name(self):
        if self.sex == "Male":
            self.user_name = "Adom"
        else:
            self.user_name = "Eve"
        return self.user_name

    def choose_sex(self):
        self.sex = random.choice(available_sex_types)
        return self.sex

    def make_id(self):
        if self.sex == "Male":
            self.id_code = f"3{self.born_date}{random.randint(1000, 9999)}"
        else:
            self.id_code = f"4{self.born_date}{random.randint(1000, 9999)}"
        return self.id_code


user1 = Human()
print(f"Name: {user1.user_name}")
print(f"Sex: {user1.sex}")
print(f"Born Date: {user1.born_date}")
print(f"Passport ID: {user1.id_code}")
