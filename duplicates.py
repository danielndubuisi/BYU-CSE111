import csv
persons_info_dict = {
    "https://example.com/1": [
        {"name": "John Michael Doe", "birthplace": "New York, USA", "dob": "1990-02-15"},
        {"name": "Emma Grace Smith", "birthplace": "London, UK", "dob": "1985-11-22"},
        {"name": "Carlos Alberto Perez", "birthplace": "Madrid, Spain", "dob": "1992-06-03"}
    ],
    "https://example.com/2": [
        {"name": "Lily Rose Williams", "birthplace": "Los Angeles, USA", "dob": "1991-08-12"},
        {"name": "David John Adams", "birthplace": "Toronto, Canada", "dob": "1987-04-18"},
        {"name": "Sophia Marie Johnson", "birthplace": "Sydney, Australia", "dob": "1993-12-09"}
    ],
    "https://example.com/3": [
        {"name": "Lucas Scott Brown", "birthplace": "Chicago, USA", "dob": "1988-01-27"},
        {"name": "Olivia Jane Green", "birthplace": "Paris, France", "dob": "1990-07-14"},
        {"name": "Miguel Angel Rivera", "birthplace": "Mexico City, Mexico", "dob": "1991-10-21"}
    ],
    "https://example.com/4": [
        {"name": "Alexander Robert Clark", "birthplace": "San Francisco, USA", "dob": "1986-03-06"},
        {"name": "Charlotte Isabelle Evans", "birthplace": "London, UK", "dob": "1994-09-17"},
        {"name": "Juan Pablo Garcia", "birthplace": "Buenos Aires, Argentina", "dob": "1990-05-24"}
    ],
    "https://example.com/5": [
        {"name": "Emily Grace Hall", "birthplace": "Vancouver, Canada", "dob": "1992-11-30"},
        {"name": "Thomas William Davis", "birthplace": "Houston, USA", "dob": "1989-02-08"},
        {"name": "Isabella Rose Martinez", "birthplace": "Barcelona, Spain", "dob": "1995-07-11"}
    ],
    "https://example.com/6": [
        {"name": "Benjamin Edward Wilson", "birthplace": "Boston, USA", "dob": "1984-10-10"},
        {"name": "Chloe Marie Taylor", "birthplace": "Dublin, Ireland", "dob": "1992-05-01"},
        {"name": "Raul Emilio Fernandez", "birthplace": "Madrid, Spain", "dob": "1991-03-17"}
    ],
    "https://example.com/7": [
        {"name": "Zoe Victoria Harris", "birthplace": "Atlanta, USA", "dob": "1994-06-22"},
        {"name": "Daniel Robert Nelson", "birthplace": "Manchester, UK", "dob": "1988-02-25"},
        {"name": "Sofia Teresa Castro", "birthplace": "Lisbon, Portugal", "dob": "1993-12-05"}
    ],
    "https://example.com/8": [
        {"name": "William James Turner", "birthplace": "New York, USA", "dob": "1990-04-09"},
        {"name": "Grace Ann Parker", "birthplace": "Melbourne, Australia", "dob": "1993-10-14"},
        {"name": "Antonio Carlos Lima", "birthplace": "Sao Paulo, Brazil", "dob": "1987-09-28"}
    ],
    "https://example.com/9": [
        {"name": "Charlotte Elizabeth King", "birthplace": "London, UK", "dob": "1995-01-23"},
        {"name": "Lucas Daniel White", "birthplace": "Los Angeles, USA", "dob": "1991-11-16"},
        {"name": "Adriana Lucia Gomez", "birthplace": "Bogotá, Colombia", "dob": "1992-05-05"}
    ],
    "https://example.com/10": [
        {"name": "Ethan Michael Scott", "birthplace": "Seattle, USA", "dob": "1986-02-20"},
        {"name": "Mia Nicole Clark", "birthplace": "Houston, USA", "dob": "1994-03-08"},
        {"name": "Diego Alejandro Morales", "birthplace": "Mexico City, Mexico", "dob": "1990-12-12"}
    ],
    "https://example.com/11": [
        {"name": "Ella Grace Anderson", "birthplace": "Paris, France", "dob": "1993-07-23"},
        {"name": "Jack Thomas Robinson", "birthplace": "Toronto, Canada", "dob": "1985-05-17"},
        {"name": "Carla Sofia Hernandez", "birthplace": "Madrid, Spain", "dob": "1991-09-14"}
    ],
    "https://example.com/12": [
        {"name": "Liam Samuel Mitchell", "birthplace": "Chicago, USA", "dob": "1992-03-18"},
        {"name": "Amelia Lily Green", "birthplace": "Bristol, UK", "dob": "1991-01-29"},
        {"name": "Juan Carlos Herrera", "birthplace": "Buenos Aires, Argentina", "dob": "1988-08-23"}
    ],
    "https://example.com/13": [
        {"name": "Mason Alexander Lee", "birthplace": "San Diego, USA", "dob": "1994-09-04"},
        {"name": "Emily Rose Moore", "birthplace": "Vancouver, Canada", "dob": "1990-12-19"},
        {"name": "Santiago Javier Ruiz", "birthplace": "Santiago, Chile", "dob": "1992-11-02"}
    ],
    "https://example.com/14": [
        {"name": "Oliver Lucas Harris", "birthplace": "Dallas, USA", "dob": "1987-06-10"},
        {"name": "Sophia Lily Evans", "birthplace": "London, UK", "dob": "1991-04-05"},
        {"name": "Miguel Enrique Castillo", "birthplace": "Caracas, Venezuela", "dob": "1990-03-13"}
    ],
    "https://example.com/15": [
        {"name": "Maya Grace Adams", "birthplace": "New York, USA", "dob": "1995-10-30"},
        {"name": "Aiden Robert Johnson", "birthplace": "Los Angeles, USA", "dob": "1992-02-28"},
        {"name": "Carlos Rafael Perez", "birthplace": "Barcelona, Spain", "dob": "1994-01-25"}
    ],
    "https://example.com/16": [
        {"name": "Evelyn Kate Clark", "birthplace": "San Francisco, USA", "dob": "1990-07-01"},
        {"name": "Oliver Nathaniel King", "birthplace": "Toronto, Canada", "dob": "1993-04-12"},
        {"name": "Ana Sofia Silva", "birthplace": "Lisbon, Portugal", "dob": "1992-09-16"}
    ],
    "https://example.com/17": [
        {"name": "Mackenzie Brooke Moore", "birthplace": "Houston, USA", "dob": "1991-06-09"},
        {"name": "Charlie Matthew White", "birthplace": "London, UK", "dob": "1988-08-20"},
        {"name": "Eduardo Pablo Martinez", "birthplace": "Mexico City, Mexico", "dob": "1993-02-18"}
    ],
    "https://example.com/18": [
        {"name": "Landon Oliver Harris", "birthplace": "Atlanta, USA", "dob": "1989-01-30"},
        {"name": "Chloe Mae Williams", "birthplace": "Melbourne, Australia", "dob": "1994-11-09"},
        {"name": "Giovanni Antonio Ricci", "birthplace": "Rome, Italy", "dob": "1991-05-22"}
    ],
    "https://example.com/19": [
        {"name": "Grace Olivia Young", "birthplace": "New York, USA", "dob": "1994-12-01"},
        {"name": "Henry Samuel Baker", "birthplace": "Los Angeles, USA", "dob": "1990-06-25"},
        {"name": "Isabella Alexandra Costa", "birthplace": "Rio de Janeiro, Brazil", "dob": "1992-07-30"}
    ],
    "https://example.com/20": [
        {"name": "Ava Isabelle Turner", "birthplace": "Seattle, USA", "dob": "1993-02-10"},
        {"name": "Maya Grace Adams", "birthplace": "New York, USA", "dob": "1995-10-30"},
        {"name": "Diego Alejandro Morales", "birthplace": "Mexico City, Mexico", "dob": "1990-12-12"}
    ]
}

csv_data = []

for link, people in persons_info_dict.items():
    for person in people:
        first_name, middle_name, surname = person["name"].split(" ", 2)
        csv_data.append([link, first_name, middle_name, surname, person["dob"], person["birthplace"]])

# Write to CSV
with open('people_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["link", "first name", "middle name", "surname", "dob", "birthplace"])
    writer.writerows(csv_data)
    
#This code will create a CSV file with the following columns: link, first name, middle name, surname, dob, and birthplace.



def compare_persons(person1, person2):
    # compare based on name, birthplace and dob
    return person1["name"] == person2["name"] and person1["birthplace"] == person2["birthplace"] and person1["dob"] == person2["dob"]


def get_duplicates(persons_info_dict):
    duplicate_person = []
    links_list = []
    keys = list(persons_info_dict.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            key1 = keys[i]
            key2 = keys[j]
            for person1 in persons_info_dict[key1]:
                for person2 in persons_info_dict[key2]:
                    if compare_persons(person1, person2):
                        duplicate_person.append(person1)
                        links_list.append(f'key1 - {key1}, key2 - {key2}')
    
    return duplicate_person, links_list


def main():
    duplicates = get_duplicates(persons_info_dict)
    print("Duplicate persons found:")
    if len(duplicates) > 0:
        for [person, link_list] in duplicates:
            print([person, link_list])
    else:
        print("No duplicates found")



if __name__ == "__main__":
    main()