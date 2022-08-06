def vacation_title(func):
    def wrapper(*args, **kwargs):
        print("Title \nCEO Red Bull Inc. \nMr. John Bigbul\n")
        return func(*args, **kwargs)
    return wrapper


@vacation_title
def vacation_vacation(first_name, surname, from_date, to_date):
    print(f"Hi John,\nI need the paid vacation from {from_date} to {to_date}.\n{first_name} {surname}")


@vacation_title
def vacation_sick_leave(first_name, surname, from_date, to_date):
    print(f"Hi John,\nI need the paid sick leave from {from_date} to {to_date}.\n{first_name} {surname}")


@vacation_title
def vacation_day_off(first_name, surname, from_date, to_date):
    print(f"Hi John,\nI need the paid day off from {from_date} to {to_date}.\n{first_name} {surname}")


def vacation_request():
    vac_type = input("Напишіть тип відпустки, який вам потрібен: \"vacation\", \"sick leave\" або \"day off\"\nВвід:").lower()
    if vac_type != "vacation" and vac_type != "sick leave" and vac_type != "day off":
        print("Не вірний тип відпустки!\nПриймається тільки один з: \"vacation\", \"sick leave\" або \"day off\"")
    else:
        first_name = input("Напишіть ваше ім'я: ")
        surname = input("Напишіть вашу фамілію: ")
        from_date = input("Напишіть дату початку відпустки(Наприклад 21/06): ")
        to_date = input("Напишіть дату закінчення відпустки(Наприклад 21/07): ")
        if vac_type == "vacation":
            vacation_vacation(first_name, surname, from_date, to_date)
        elif vac_type == "sick leave":
            vacation_sick_leave(first_name, surname, from_date, to_date)
        elif vac_type == "day off":
            vacation_day_off(first_name, surname, from_date, to_date)


if __name__ == "__main__":
    vacation_request()
