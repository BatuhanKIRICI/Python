country = input("Enter country name: ")
visits = int(input("Enter number of times visited: "))
list_of_cities = eval(input("Enter the cities you've visited: "))

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Nantes", "Marseille"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Weimar", "Dortmund"],
        "total_visits": 5,
    },
]


travel_log_2 = [{"country": "", "cities_visited": [], "total_visits": 0}]


def add_new_country(country, visits, list_of_cities):

    travel_log_2 = {}
    travel_log_2["country"] = country
    travel_log_2["cities_visited"] = list_of_cities
    travel_log_2["total_visits"] = visits
    travel_log.append(travel_log_2)


add_new_country(country, visits, list_of_cities)

print(
    f"""I've been to {travel_log[2]["country"]} {travel_log[2]["total_visits"]} times.
    And visited {travel_log[2]["cities_visited"][1]} mostly."""
)
