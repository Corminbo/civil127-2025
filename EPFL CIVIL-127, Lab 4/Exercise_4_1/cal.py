class Cal:
    def __init__(self):
        # Initialise les valeurs par défaut pour l'année, le mois et le jour de début de la semaine
        self.year_value = 2025
        self.month_value = "jan"
        self.week_start_value = "monday"
        self.mounth_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.week_start_name = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  
    def year(self, year):
        # Définit l'année pour le calendrier
        self.year_value = year

    def month(self, month):
        # Définit le mois pour le calendrier
        month_names = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        self.month_value = month_names.index(month.lower()) + 1

    def week_start(self, week_start):
        # Définit le jour de début de la semaine pour le calendrier
        self.week_start_value = week_start.lower()

    def print(self):
        # Affiche le calendrier formaté pour le mois et l'année spécifiés
        pass  # Implémentez la logique d'affichage ici

    
if __name__ == "__main__":
    c = Cal()
    c.year(2025)
    c.month("jan")
    c.week_start("sun")
    c.print()