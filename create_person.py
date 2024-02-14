from faker import Faker
import os 


fake = Faker('en_uk')

def fake_person():
    person = fake.name() 
    split_person = person.rsplit()
    surname = split_person[-1]
    address = fake.address()
    file = open(surname + ".txt", "w")
    file.write(person + "\n" + address)
    file.close() 
    return surname

file_name = fake_person() + ".txt"


os.rename(f"/Users/muhtadimaahir/QA_Projects/extending-testing/phase2/03_resources/{file_name}", f"/Users/muhtadimaahir/QA_Projects/extending-testing/phase2/03_resources/target_directory/updates/{file_name}")

os.rename(f"/Users/muhtadimaahir/QA_Projects/extending-testing/phase2/03_resources/{file_name}", f"target_directory/originals/{file_name}")

