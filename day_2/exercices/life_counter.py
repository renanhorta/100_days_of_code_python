from datetime import datetime
def life_counter(age):
    last_age = 90
    current_year = datetime.now().year
    user_birth_year = (current_year - int(age))
    last_user_year = (user_birth_year + last_age)
    years_left = (last_user_year - current_year)
    mount_left = round(years_left * 12)
    weaks_left = round(years_left * 52 )
    days_left =round(years_left * 365)

    print(f"Você tem {days_left} dias, {weaks_left} semanas e {mount_left} meses faltando até seus 90 anos.")

user_age = input("Quantos anos você tem?")

life_counter(user_age)