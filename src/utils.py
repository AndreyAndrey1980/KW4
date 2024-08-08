from src.api import HH_Api
from src.json_worker import JSONSaver
from src.vacancy import Vacancies


def write_or_dont_write(vac_list: Vacancies) -> None:
    """Принимает список вакансий, и записывает его в json-файл."""

    print("Записать полученные данные в JSON файл?")
    user_answer = input("Да/Нет ").lower().strip()
    if user_answer != "да":
        print("Спасибо за использование программы!")
    else:
        jsonfile = JSONSaver("vacancies.json")
        jsonfile.write_to_file(vac_list)
        print("Данные успешно записаны.\n")


def valid_input(message: str) -> int | None:
    """Если возможно, переводит str в int, иначе предлагает ввести число."""
    while True:
        count = input(message).strip()
        if count.isdigit():
            return int(count)
        else:
            print("Можно ввести только целое число")


def main_menu() -> int:
    """Реализация главного меню, возвращает номер меню"""

    print(
        "1 - Вывести все вакансии.\n"
        "2 - Вывести топ-n вакансий по зарплате.\n"
        "3 - Выборка по городу.\n"
        "4 - Выборка по зарплате.\n"
        "5 - Удалить вакансию.\n"
        "6 - Записать результаты в файл.\n"
        "7 - Выход.\n"
    )

    while True:
        answer = input("Выберите действие: ").strip()
        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= 7:
                break
            else:
                print("Можно ввести только число от 1 до 7!")
        else:
            print("Можно ввести только целое число")
    print("*" * 50)
    return answer


def user_interaction() -> None:
    """Основная функция по взаимодействию с пользователем"""

    print("Здравствуйте! \nЭта программа по поиску и сравнению вакансий на HeadHunter. \n")
    keyword = input("Введите ключевые слова для поиска вакансий: ").strip().split()
    hh_api = HH_Api()
    while True:
        pages = input("Введите количество страниц для вывода: ").strip()
        if pages.isdigit():
            pages = int(pages)
            break
        else:
            print("Можно ввести только число!")

    vac_list = hh_api.get_vacancies(keyword, pages)

    print("*" * 50)
    print('Список вакансий с сайта "HeadHunter":')
    print("-" * 50)
    print(f"Найдено {len(vac_list)} вакансий: \n")
    last_choice = Vacancies()
    while True:
        answer = main_menu()
        if answer == 1:
            vac_list = hh_api.get_vacancies(keyword, pages)
            print(vac_list)
            last_choice = vac_list
            print(f"Всего {len(vac_list)} вакансий\n")

        elif answer == 2:
            top_n = valid_input("Введите количество вакансий: ")
            top_n_vac = vac_list.get_top_n_vacancy(top_n)
            print("*" * 50, f"\nТоп {len(top_n_vac)} - вакансий:\n")
            print(top_n_vac)
            last_choice = top_n_vac

        elif answer == 3:
            city = input("Введите название города: ").strip().lower()
            by_city = vac_list.filtered_by_city(city)
            print(f"Найдено {len(by_city)} вакансий\n")
            if len(by_city) > 0:
                show = input("Вывести результат на экран? Да/Нет ").strip().lower()
                if show == "да":
                    print(by_city)
            last_choice = by_city

        elif answer == 4:
            salary_from = valid_input("Введите размер зарплаты: ")
            by_salary = vac_list.filtered_by_salary(salary_from)
            print(f"Найдено {len(by_salary)} вакансий\n")
            if len(by_salary) > 0:
                show = input("Вывести результат на экран? Да/Нет ").strip().lower()
                if show == "да":
                    print(by_salary)
            last_choice = by_salary

        elif answer == 5:
            vac_id = valid_input("Введите id вакансии: ")
            if last_choice:
                len_list = len(last_choice)
                last_choice.delete_vacancy(vac_id)
            else:
                len_list = len(vac_list)
                vac_list.delete_vacancy(vac_id)
                last_choice = vac_list
            if len_list == len(last_choice):
                print("Вакансия с таким id не найдена\n")
            else:
                print(f"Удалена вакансия с id={vac_id}\nОсталось {len(last_choice)} вакансий\n")
            if len(last_choice) > 0:
                print(last_choice)
            print(f"Всего  {len(last_choice)} вакансий\n")

        elif answer == 6:
            jsonfile = JSONSaver("vacancies.json")
            jsonfile.write_to_file(last_choice)
            print("Данные успешно записаны.\n")

        elif answer == 7:
            print("Благодарим за использование программы.\n До свидания.")
            break
