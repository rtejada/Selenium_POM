import json
opportunity = {'name_opportunity': 'Traime un amigo', 'close_date': '31/07/2020', 'amount_opprtunity': '1500', 'type': 'Tournefeuille',
             'tel': '034-829875', 'mobile': '689457815', 'workingStation': 'Administrativo', 'departament': 'Toulose_Depart',
             'email': '@toulouse.fr', 'address': '138 Saint-Geniès-Bellevue', 'city': 'Saint-Bellevue', 'cp': '31200',
             'country': 'Francia', 'description': 'Explicit expectations available only for Selenium customers'}


file = open("data_opportunity.json", "w")
json.dump(opportunity, file)
file.close()
