# -*- coding: utf-8 -*-       
import random
import string 
intent_keywords = {"hallo": "hallo",
                  "vertretungsplan": "vertretungsplan",
                  "öffnungszeiten": "öffnungszeiten",
                  "wie geht es dir": "wie geht es dir",
                  "wie gehts dir": "wie geht es dir",
                  "5": "öffnungszeiten",

                  }

random_answers = ["Interessant ...", "Ich verstehe ...", "Leider habe ich hierauf keine passende Antwort.", "Können Sie die Frage anders formulieren?"]

intent_answers = {"hallo": "Hallo, wie kann ich Ihnen helfen?",
                  "vertretungsplan": "Der Vertretungsplan der ITECH ist im Bereich Service auf der Homepage www.itech-bs14.de verlinkt.",
                  "öffnungzeiten": "Das Schulbüro der ITECH hat zu folgenden Zeiten geöffnet: Mo - Fr 07:30 - 11:45 Uhr / Do 12:45 - 17:00 Uhr.",
                  "Wie geht es dir": "Mir geht es gut, was benötigen Sie?",
                  "help": "Hier sehen Sie mögliche Befehle, die aktuell ausführbar sind.",
                  "Mensch": "Nein, ich bin eine KI.",
                  "Robotter": "Ja.",
                  "Webex": "Schauen Sie in den Klassenkurs, um den jeweiligen Raum zu finden, den finden Sie unter moodle.itech-bs14.de",
                  "Lehrer": "Sie finden die zuständigen (Klassen-)lehrer unter Ihrem Klassenkurs, in der Kategorie: Klassenkursorganisation.",
                  "Stundenplan": "Den jeweiligen Stundenplan finden Sie im Klassenkurs unten verlinkt.",
                  "Telefonnummer": "Die Telefonnummer unseres Sekräteriats ist: 040 4287940",
                  "Vertretungsplan": "Der Link für den Vertretungsplan ist folgender: https://stundenplan.hamburg.de/WebUntis/monitor?school=hh5918&monitorType=subst&format=FgarV5344HGhuasdfz",
                  "Krankenmeldung": "Wenn Sie Krank sind melden Sie sich bitte in Ihrem jeweiligen Betrieb krank und schreiben eine E-Mail an Ihren Klassenlehrer und den jeweiligen Fachlehrer für den Tag.",
                  "Email": "Unsere Schulemail lautet: bs14@hibb.hamburg.de"
                  }

print("Willkommen zum ITECH-Chatbot")
print("Für Beispiele schreiben sie help in den Chat.")
print("Wenn Sie das Programm beenden möchten, schreiben sie eifach 'bye' in den Chat.")
print("")

user_input = ""  #Variable wird als leerer String initialisiert
while user_input != "bye": 
    user_input = ""
    while user_input == "":
        user_input = input("Wie kann ich Ihnen helfen? ")

    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    user_words = user_input.split()
    
    for words in user_words: 
        if words in "help" or "Help" or "hilfe" or "Hilfe":
            print(intent_answers["help"])
            x=0
            while x < 3:
                print(random.choice(list(intent_keywords.keys())))
                x= x+1
        elif words in intent_keywords:
            print(intent_keywords[words])
        else:
            print(random.choice(random_answers))

print("Vielen Dank, dass sie . Bis zum nächsten mal.")
