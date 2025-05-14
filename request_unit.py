import requests


def highest_international_students(firstCity, secondCity):
    url = "https://jsonmock.hackerrank.com/api/universities"
    page = 1
    universities = []

    while True:
        response = requests.get(url, params={"page": page})
        data = response.json()
        universities.extend(data["data"])

        if page >= data["total_pages"]:
            break
        page += 1

    def get_top_university_by_city(city):
        city_unis = [uni for uni in universities if uni["location"]["city"].lower() == city.lower()]
        if not city_unis:
            return None
        return max(city_unis, key=lambda u: int(u["international_students"].replace(",", "")))["university"]

    top_uni = get_top_university_by_city(firstCity)
    if top_uni:
        return top_uni
    else:
        return get_top_university_by_city(secondCity)


print(highest_international_students("London", "Paris"))
