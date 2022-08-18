############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self,
        name,
        code,
        first_harvest,
        color,
        is_seedless,
        is_bestseller,
    ):
        """Initialize a melon."""
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", "Casaba", 2003, "orange", True, True)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
        "yw", "Yellow Watermelon", 2013, "yellow", False, True
    )
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # desired output: "{melon} pairs with: {pairing}"

    for melon in melon_types:
        print(f"{melon.name} pairs with:")
        for pairing in melon.pairings:
            print(f"{pairing}\n\n")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # key: codes, as strings
    # values: melon type for that code
    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon.name

    return melon_dict


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(
        self,
        type,
        shape_rating,
        color,
        harvest_field,
        harvester,
        is_sellable,
    ):
        """Initialize a melon."""
        self.type = type
        self.shape_rating = shape_rating
        self.color = color
        self.harvest_field = harvest_field
        self.harvester = harvester
        self.is_sellable = is_sellable

    def is_sellable(self):
        if self.shape_rating > 5 and self.color > 5 and self.harvest_field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # identifies melon name by code via make_melon_type_lookup(),
    # then it inputs into instance below
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Michael")

    melons = [
        melon_1,
        melon_2,
        melon_3,
        melon_4,
        melon_5,
        melon_6,
        melon_7,
        melon_8,
        melon_9,
    ]

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        harvester = f"Harvested by {melon.harvester}"
        harvest_field = f"Field #{melon.harvest_field}"
        status = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE"
        print(f"{harvester} from {harvest_field} {status}")

# write function that opens and loops over file, 
# create melon object for each file in file
# file has 5 elements ------
#  Shape, Color, Type, Harvested_By, Field


harvest_melons = []

def process_log(log_file,Melons,get_sellability_report):
    with open("harvest_log.txt") as file:
        for line in file:
            # iterate through lines and pull info for each variable by slicing
            shape_rating = line[6:8]
            color = line[14:16]
            code = line[21:24]
            harvester = line[37:44]
            field = line[52:]
        harvest_melons.append(Melon(
            shape_rating = shape_rating,
            color = color,
            code = code,
            harvester=harvester,
            harvest_field=field,))
            
        
        print(harvest_melons)
 
get_sellability_report(harvest_melons)

# process_log(log_file="harvest_log.txt", Melons=Melon)


    
