import datetime

class Cal:
    def __init__(self):
        today = datetime.date.today()  # On récupère la date d'aujourd'hui
        self._year = today.year  # Année par défaut
        self._month = today.month  # Mois par défaut
        self._week_start = "mon"  # Par défaut, la semaine commence lundi

    def year(self, year):
        # Met à jour l'année du calendrier
        self._year = year

    def month(self, month_str):
        # Met à jour le mois du calendrier en utilisant une chaîne de caractères
        months = ["jan", "feb", "mar", "apr", "may", "jun",
                  "jul", "aug", "sep", "oct", "nov", "dec"]
        if month_str.lower() in months:
            self._month = months.index(month_str.lower()) + 1
        else:
            raise ValueError("Invalid month format. Use 'jan', 'feb', etc.")

    def week_start(self, day):
        # Définit le premier jour de la semaine (lundi ou dimanche)
        if day.lower() in ["mon", "sun"]:
            self._week_start = day.lower()
        else:
            raise ValueError("week_start must be 'mon' or 'sun'.")

    def print(self):
        # Affiche le calendrier pour le mois et l'année spécifiés
        first_day = datetime.date(self._year, self._month, 1)  # Premier jour du mois

        if self._month == 12:
            total_days = 31  # Décembre a toujours 31 jours
        else:
            next_month = datetime.date(self._year, self._month + 1, 1)
            total_days = (next_month - datetime.timedelta(days=1)).day
        
        month_name = first_day.strftime("%B")  # Convertit 2025-01-01 → "January"
        print(f"    {month_name} {self._year}")  # Format "    January 2025"
        
        # Définir les étiquettes des jours de la semaine en fonction du premier jour de la semaine
        days_labels = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"] if self._week_start == "mon" \
                      else ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        print(" ".join(days_labels))  # Affiche : "Su Mo Tu We Th Fr Sa"
        
        # Calculer l'index du premier jour du mois
        start_index = first_day.weekday()  # 0 = Lundi, 6 = Dimanche
        if self._week_start == "sun":
            start_index = (start_index + 1) % 7  # Ajuste si dimanche est premier jour
        
        # Créer une liste de jours avec des espaces pour les jours avant le début du mois
        days = ["   "] * start_index + [f"{day:2} " for day in range(1, total_days + 1)]
        
        # Afficher les jours du mois, 7 jours par ligne
        for i in range(0, len(days), 7):
            print("".join(days[i:i+7]))