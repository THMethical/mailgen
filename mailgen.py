import random
import string

jobs = ["Architekt", "Anwalt", "Apotheker", "Arzt", "Bäcker", "Bauingenieur", "Bauarbeiter", "Buchhalter", "Controller", "Dachdecker", "Datenanalyst",
        "Datenbankadministrator", "Designer", "Detektiv", "Elektriker", "Entwickler", "Erzieher", "Eventmanager", "Fahrlehrer", "Feuerwehrmann",
        "Finanzanalyst", "Fotograf", "Friseur", "Grafikdesigner", "Handwerker", "Heilpraktiker", "Informatiker", "Ingenieur", "Journalist",
        "Kellner", "Kfz-Mechaniker", "Koch", "Krankenpfleger", "Künstler", "Landwirt", "Landschaftsgärtner", "Lehrer", "Lektor", "Logopäde",
        "Maler", "Manager", "Marketingmanager", "Maschinenbauer", "Maurer", "Mechaniker", "Mediengestalter", "Mediziner", "Metzger", "Mitarbeiter im Kundenservice",
        "Musiker", "Notarzt", "Optiker", "Organisationsentwickler", "Pfarrer", "Pilot", "Polizist", "Projektmanager", "Psychologe", "Redakteur",
        "Rechtsanwalt", "Reinigungskraft", "Schauspieler", "Sekretär", "Sicherheitsmitarbeiter", "Softwareentwickler", "Soldat", "Steuerberater",
        "Stylist", "Systemadministrator", "Tänzer", "Techniker", "Tierarzt", "Übersetzer", "Verkäufer", "Versicherungsmakler", "Videoproduzent",
        "Webentwickler", "Werbegrafiker", "Winzer", "Wissenschaftler", "Zahnarzt", "Zimmermann", "Zoologe"]


hobbies = ["reisen", "lesen", "gärtnern", "kochen", "sport", "musik", "tanzen", "malen", "schreiben", "fotografieren",
          "wandern", "schwimmen", "zeichnen", "radfahren", "yoga", "klettern", "campen", "filme schauen", "videospiele",
          "gitarre spielen", "klavier spielen", "singen", "tischtennis", "billard", "bowling", "tennis", "basketball",
          "fußball", "baseball", "boxen", "kickboxen", "karate", "judo", "schach", "poker", "zaubern", "modellbau",
          "cosplay", "rollenspiele", "fantasy-literatur", "wissenschaft", "astronomie", "geschichte", "sprachen lernen",
          "kalligrafie", "origami", "stricken", "nähen", "basteln", "kochen", "backen", "grillen", "weinproben", "cocktails mixen",
          "barista-kunst", "bierbrauen", "fotobearbeitung", "webdesign", "programmieren", "datenanalyse", "robotik", "elektronik",
          "3D-Druck", "filmen", "schneiden", "fotografie", "videobearbeitung", "make-up", "frisieren", "mode", "youtuber",
          "podcaster", "bloggen", "social media", "recherche", "journalismus", "freiwilligenarbeit", "umweltschutz", "tierpflege",
          "karitative Arbeit", "politik", "philosophie", "religion", "spiritualität", "meditation", "pilgern", "reiten", "segeln",
          "surfen", "tauchen", "skifahren", "snowboarden", "schlittschuhlaufen", "snowshoeing"]

names = ["Emma", "Noah", "Olivia", "Liam", "Ava", "William", "Sophia", "Mason", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Jacob", "Amelia", "Michael", 
         "Evelyn", "Ethan", "Abigail", "Daniel", "Emily", "Matthew", "Harper", "Logan", "Elizabeth", "Lucas", "Sofia", "Jackson", "Avery", "David", "Ella", "Oliver", 
         "Madison", "Joseph", "Scarlett", "Samuel", "Grace", "Henry", "Chloe", "Owen", "Victoria", "Sebastian", "Riley", "Gabriel", "Aria", "Elijah", "Lily", "Caleb", 
         "Aurora", "Sophie", "Nathan", "Isabelle", "Daniel", "Alexandra", "Connor", "Makayla", "Luke", "Aaliyah", "Logan", "Alyssa", "Ryan", "Hannah", "Christian", "Addison", 
         "Evan", "Ellie", "Levi", "Mackenzie", "Isaac", "Brooklyn", "Tyler", "Peyton", "Aiden", "Audrey", "Eli", "Anna", "Nolan", "Aubrey", "Adam", "Kaitlyn", "Brayden", 
         "Ava", "Evelyn", "Bryce", "Mia", "Max", "Lila", "Cameron", "Leah", "Jacob", "Natalie", "Ian", "Sarah", "Lucy", "Katherine", "Eric", "Claire", "Blake", 
         "Julia", "Jaxon", "Kaylee", "Grayson", "Lillian", "Miles", "Lauren", "Gavin", "Samantha", "Caroline", "Taylor", "Elena", "Chase", "Ellie", "Colton", 
         "Victoria", "Dominic", "Brielle", "Maddox", "Kylie", "Jace", "Avery", "Cooper", "Piper", "Landon", "Jocelyn", "Tristan", "Penelope", "Gage", "Morgan", 
         "Hudson", "Jasmine", "Parker", "Aria", "Derek", "Faith", "Carter", "Autumn", "Caleb", "Annabelle", "Jason", "Bella", "Austin", "Stella", "Axel", "Skylar", 
         "Bennett", "Eva", "Micah", "Sadie", "Brady", "Lucia", "Roman", "Katie", "Xavier", "Makenna", "Leo", "Allison", "Wyatt", "Clara", "Ezra", "Genevieve", "Graham", 
         "Liliana", "Camden", "Nora", "Oscar", "Hailey", "Tucker", "Gabrielle", "Jude", "Kinsley", "Silas", "Adeline", "Kai", "Rylee", "Emmett", "Emilia", "Finn", "Cecilia", 
         "George", "Aubree", "Colin", "Delilah", "Rhett", "Ivy", "Leo", "Juliana", "Reid", "Isabel"]


def generate_email(category, domain, num):
    emails = []
    for i in range(num):
        if category == "jobs":
            username = random.choice(jobs)
        elif category == "hobbies":
            username = random.choice(hobbies)
        elif category == "names":
            username = random.choice(names)
        else:
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = username + str(random.randint(0, 1000)) + "@" + domain
        emails.append(email)
    return emails

domain = input("Provider angeben zb blablabla.com: ")
num_emails = int(input("Wie viele E-Mails moechten Sie erstellen? "))
category = input("Welche Kategorie moechten Sie verwenden? (jobs, hobbies, names) ")

emails = generate_email(category, domain, num_emails)
print(emails)

with open('email_list.txt', 'w') as f:
    for email in emails:
        f.write(email + '\n')
