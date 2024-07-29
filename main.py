from src.get_api_hh import get_api_hh
from src.json_saver import json_saver
from src.vacancy import vacancy

response = get_api_hh()

while True:
    user_vacancy: str = input("Text name vacancy for search:\n")
    user_city: str = input("Text city in where you want to find vacancies:\n")
    if isinstance(user_city, str) and isinstance(user_vacancy, str):
        break
    print(f"Please, text alpha, not {user_city}")

while True:
    user_salary = input("Text min salary for search:\n")
    if user_salary.isdigit():
        break
    print(f"Please, text digit, not {user_salary}")

# Get vacancies for user
response.get_vacancy_from_api(user_vacancy)

file_json = json_saver()

# Save response to JSON
file_json.save_file(response.all_vacancy)

# Read JSON file
file_vacancies = file_json.read_file()

# Print vacancies for user
vacancy = vacancy.get_vacancy_list(file_vacancies, user_city, int(user_salary))
sorted_vacancies = sorted(vacancy)

while True:
    count = input("How vacancies do you want to see:\n")
    if count.isdigit():
        break
    print(f"Please, text digit, not {count}")

print(*sorted_vacancies[:int(count)])