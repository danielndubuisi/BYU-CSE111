# import requests
# from bs4 import BeautifulSoup
# import time
# from fake_useragent import UserAgent

# def main():
#     url = 'https://www.familysearch.org/search/linker?pal=/ark:/61903/1:1:6KWH-3JY5&id=LB9F-478&cid=byurll'
#     username = 'username' #supply valid username
#     password = 'password' # supply valid password
#     html_content = get_website_data(url, username, password)
#     if html_content:
#         data = extract_data(html_content)
#         print(data)


# def get_website_data(url, username, password):
#     """
#     Fetches the HTML content of a given URL with authentication.

#     Args:
#         url: The URL of the website to fetch.
#         username: The username for authentication.
#         password: The password for authentication.

#     Returns:
#         The HTML content of the website as a string.
#     """
#     user_agent = UserAgent().chrome  # Get a random Chrome user-agent
#     headers = {'User-Agent': user_agent}
#     try:
#         response = requests.get(url, headers=headers, auth=(username, password))
#         response.raise_for_status()  # Raise an exception for bad status codes
#         time.sleep(2)  # Introduce a 2-second delay
#         return response.text
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching URL: {e}")
#         return None


# def extract_data(html_content):
#     """
#     Extracts relevant data from the HTML content.

#     Args:
#         html_content: The HTML content of the website.

#     Returns:
#         The entire HTML content of the website.
#     """
#     soup = BeautifulSoup(html_content, 'html.parser')
#     # Return the entire HTML content
#     extracted_data = soup.prettify()
#     return extracted_data


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
        {"name": "Guan M. Doe", "birthplace": "New York, USA", "dob": "1990-02-15"},
        {"name": "Ema Grace Smith", "birthplace": "London, UK", "dob": "1985-11-22"},
        {"name": "C. A. Perez", "birthplace": "Madrid, Spain", "dob": "1992-06-03"}
    ],
        "https://example.com/21": [
        {"name": "Liam Rodney Williams", "birthplace": "Las Palmas, USA", "dob": "1981-08-12"},
        {"name": "Dave John Adams", "birthplace": "Ontario, Canada", "dob": "1987-08-18"},
        {"name": "Sophia Marie Johnson", "birthplace": "Sydney, Australia", "dob": "1998-12-09"}
    ],
        "https://example.com/22": [
        {"name": "L Sidney Williams", "birthplace": "Las Palmas, USA", "dob": "1981-08-12"},
        {"name": "Austin Guan Adams", "birthplace": "Ontario, Canada", "dob": "1987-08-18"},
        {"name": "Johnson Marie Sophia", "birthplace": "Sydney, Australia", "dob": "1998-12-09"}
    ],
}


# Nuances to consider:
# same person - different name / surname (common among women)
# same person - different dob but name and place of birth match
# same person - different spelling of name or two of three initials match

def compare_initials(person1, person2):
    person1_initials = get_initials_from_person(person1)
    person2_initials = get_initials_from_person(person2)

    person1 = person1_initials.split('. ') # ['J', 'M', 'D']
    person2 = person2_initials.split('. ') # ['K', 'D', 'M']

    # check if two of three initials match
    if (person1[0] == person2[0] or person1[0] == person2[1] or person1[0] == person2[2]) and (person1[1] == person2[0] or person1[1] == person2[1] or person1[1] == person2[2]):
        return True
    elif (person1[0] == person2[0] or person1[0] == person2[1] or person1[0] == person2[2]) and (person1[2] == person2[0] or person1[2] == person2[1] or person1[2] == person2[2]):
        return True
    elif (person1[1] == person2[0] or person1[1] == person2[1] or person1[1] == person2[2]) and (person1[2] == person2[0] or person1[2] == person2[1] or person1[2] == person2[2]):
        return True
    else:
        return False
        

def get_initials_from_person(person: dict):

    names = person["name"].strip().split(' ')
    initials = []
    for name in names:
        initials.append(name[0])

    full_initials = '. '.join(initials)
    return full_initials #J. M. D


def compare_persons(person1: dict, person2: dict):
    # compare based on name, birthplace and dob
    if(get_initials_from_person(person1) == get_initials_from_person(person2) and person1["birthplace"] == person2["birthplace"] and person1["dob"] == person2["dob"]):
        return True, "All conditions match"
    
    elif(get_initials_from_person(person1) == get_initials_from_person(person2) and person1["birthplace"] != person2["birthplace"] and person1["dob"] == person2["dob"]):
        return True, "Initials & DOB match but birthplace doesn't match"
    
    elif(get_initials_from_person(person1) == get_initials_from_person(person2) and person1["birthplace"] == person2["birthplace"] and person1["dob"] != person2["dob"]):
        return True, "Initials & birthplace match but DOB doesn't match"
    
    # update this condition to check if two of three initials match
    elif(compare_initials(person1, person2) and person1["birthplace"] == person2["birthplace"] and person1["dob"] == person2["dob"]):
        return True, "At least two initials, DOB & birthplace match"
    
    else:
        return False, None
    
    # person1["name"] == person2["name"] and person1["birthplace"] == person["birthplace"] and person["dob"] == person["dob"]
    

def get_duplicates(persons_info_dict):
    duplicate_person = []
    links_list = []
    conditions_list = []
    keys = list(persons_info_dict.keys())

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            key1 = keys[i]
            key2 = keys[j]
            for person1 in persons_info_dict[key1]:
                for person2 in persons_info_dict[key2]:
                    is_duplicate, condition = compare_persons(person1, person2)
                    if is_duplicate:
                        duplicate_person.append(person1)
                        links_list.append(f'link1 - {key1}, link2 - {key2}')
                        conditions_list.append(condition)
    
    return duplicate_person, links_list, conditions_list


def main():
    duplicate_person, link_list, conditions_list = get_duplicates(persons_info_dict)
    print(f"Duplicate persons found:\n")
    if len(duplicate_person) > 0:
        for person, link, condition in zip(duplicate_person, link_list, conditions_list):
                print(f'Person: {person} \nLinks: {link} \nCondition met: {condition} ')
                print("-----------------------------------------------------------------------------------------------------")
    else:
        print("No duplicates found")



if __name__ == "__main__":
    main()
