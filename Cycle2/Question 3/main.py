import json

# Function to read the file 'iris.json' line by line
def read_as_lines(filename):
    with open(filename, "r") as text_file:
        text_content = text_file.readlines()
    return text_content

# Function to read the file 'iris.json' as a dictionary
def read_as_dict(filename):
    with open(filename, "r") as json_file:
        json_content = json.load(json_file)
    return json_content

# Function to get the details of all flowers whose species is "setosa"
def get_flowers(dictionary_list , flower_species):
    flowers = []
    for flower in dictionary_list:
        if flower["species"] == flower_species:
            flowers.append(flower)
    return flowers

# Function to get the minimum petal area and max sepal area in each species
def get_sepal_and_petal_area(dictionary_list):
    species_list = sorted({flower["species"] for flower in dictionary_list})
    results = {}
    for species in species_list:
        sepal_areas = []
        petal_areas = []
        for flower in dictionary_list:
            if flower["species"] == species:
                sepal_areas.append(flower["sepalLength"] * flower["sepalWidth"])
                petal_areas.append(flower["petalLength"] * flower["petalWidth"])
        results[species] = {"min_sepal_area": min(sepal_areas), "max_petal_area": max(petal_areas)}
    return results

# Function to sort the list of dictionaries according to the total area are sepal and petal
def sort_by_total_area(dictionary_list):
    for flower in dictionary_list:
        total_area = flower["sepalLength"] * flower["sepalWidth"] 
        + flower["petalLength"] * flower["petalWidth"]
        total_area = round(total_area, 2)
        flower["totalArea"] = total_area
    return sorted(dictionary_list, key=lambda flower: flower["totalArea"])

# Main program
print("Welcome to the program!\n",
      "1. Read the file 'iris.json' as lines\n",
      "2. Read the file 'iris.json' as json\n",
      "3. Get the details of all flowers whose species is 'setosa'\n",
      "4. Get the minimum petal area and max sepal area in each species\n",
      "5. Sort the list of dictionaries according to the total area are sepal and petal\n",
      "6. Exit the program\n")

while True:
    choice = input("Enter your choice: ")
    print("\n---------------------------------------------------------\n")
    if choice == "1":
        print("Contents of the file 'iris.json' read as lines: ")
        contents_as_lines = read_as_lines("iris.json")
        for line in contents_as_lines:
            print(line.replace("\n", "\\n"))
    elif choice == "2":
        print("Contents of the file 'iris.json' read as json: \n")
        contents_as_json = read_as_dict("iris.json")
        for dictionary in contents_as_json:
            print(dictionary)
    elif choice == "3":
        setosa = get_flowers(read_as_dict("iris.json"), "setosa")
        for flower in setosa:
            print(flower)
    elif choice == "4":
        areas = get_sepal_and_petal_area(read_as_dict("iris.json"))
        for species in areas:
            print(f"{species}: {areas[species]}")
    elif choice == "5":
        sorted_by_area = sort_by_total_area(read_as_dict("iris.json"))
        for flower in sorted_by_area:
            print(flower)
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Enter a valid choice!")