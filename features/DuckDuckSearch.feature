# Created by jcastillo at 16/08/20
Feature: Búsqueda en DuckDuckGo
  # Enter feature description here

  Scenario: Búsqueda en DuckDuckGo
    Given Visitamos la web de duckduckgo
    When se introduce la búsqueda panda
    Then hay resultados para esa búsqueda
