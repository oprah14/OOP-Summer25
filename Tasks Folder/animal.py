# animals.py


animals = [
    {
        'name': 'Cat',
        'group': 'Mammals',
        'number_of_legs': 4,
        'skills': ['jumping', 'climbing']
    },
    {
        'name': 'Eagle',
        'group': 'Birds',
        'number_of_legs': 2,
        'skills': ['flying', 'hunting']
    },
    {
        'name': 'Shark',
        'group': 'Fish',
        'number_of_legs': 0,
        'skills': ['swimming', 'hunting']
    },
    {
        'name': 'Frog',
        'group': 'Amphibians',
        'number_of_legs': 4,
        'skills': ['jumping', 'swimming']
    },
    {
        'name': 'Snake',
        'group': 'Reptiles',
        'number_of_legs': 0,
        'skills': ['slithering', 'camouflaging']
    }
]

# Print animals data for verification
if _name_ == "_main_":
    for animal in animals:
        print(animal)

