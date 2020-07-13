import json
campaigns = {'name_campaign': 'SELENIUM-TEST', 'status': 'Active', 'description': 'Disponibles para clientes de Selenium',
             'quote': '2000', 'actual_cost': '2500', 'expected_revenue': '5000', 'expected_cost': '3200', 'impressions': '7',
             'objective': 'Conseguir Rentabilidad', 'target_list_name': 'TA', 'type': 'test', 'template_name': 'Case Creation',
             'name_marketing': 'PROM ', 'hour': '11', 'minute': '50', 'address_mail': 'Saint-Geniès-Bellevue@Toulose.fr'}


file = open("data_campaign.json", "w")
json.dump(campaigns, file)
file.close()