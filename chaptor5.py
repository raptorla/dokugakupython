musician = ["Kishidakyoudan", "Ado", "YOASOBI"]

Place = [("Hamamatsucho",), ("Yurakucho",), ("Bakurocho",)]

me = {"height": 168,
        "weight": 54,
        "eyecolor": "Brown"
}

answer = input("Type height , weight or eyecolor:")

if answer in me:
    result = me[answer]
    print(result)