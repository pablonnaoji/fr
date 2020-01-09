def create_single_part(part):
    return str(part)

def create_quantity_needed_efficiently(part_name,quantity):
    quantity_created = 0 
    quantity_needed = quantity
    parts = []
    while quantity_created < quantity_needed:
        p = create_part(part_name)
        parts.append(p)
    return parts

def final_integration(building_materials):
    vehicle = []
    for x in building_materials:
        vehicle.append(x)
    return vehicle

def build_vehicle(bom):
    vehicle = [] # vehicle is an array of components
    for x in bom: #create multiples parts first
        if x['quantity'] > 1:
            parts =  create_quantity_needed_efficiently(x['part_name'],x['quantity'])
            vehicle.append(parts)
    for x in bom: #create single parts last
        if x['quantity'] == 1:
            vehicle.append(create_single_part(x['part_name']))
    return final_integration(vehicle)
    