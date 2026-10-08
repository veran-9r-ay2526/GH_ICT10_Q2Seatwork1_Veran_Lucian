from pyscript import display, document

def get_country(e):
    document.getElementById('output').innerHTML = ""

    country = document.getElementById('country').value.title()
    nations = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
    nicknames = ["The Land of Silver",
                 "The Land of Bolívar",
                 "The Land of the Holy Cross",
                 "The Land of Poets",
                 "Coffee Capital of the World",
                 "The Land of the Four Worlds",
                 "The Land of Many Waters",
                 "The Heart of South America",
                 "The Land of the Incas",
                 "Beating Heart of the Amazon",
                 "The River of the Painted Birds",
                 "The Land of Grace"]
    position = nations.index(country)

    display("Nickname: " + nicknames[position], target="output")
