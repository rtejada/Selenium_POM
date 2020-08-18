# Created by roxana at 17/08/20
Feature: Búsqueda en Cual es mi IP
  # Enter feature description here

  Scenario: Verificar que la página "CualEsMiIp" muestra datos correctos, y para ello compararlo con otra pagina (MaxMind)
    Given Acceder a CualEsMiIp
    And Cargar Geolocalización
    When Obtener los datos
    Then Comparar resultados con MaxMind
