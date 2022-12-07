import datetime as dt
from typing import Tuple
from xml.etree import ElementTree as ET

PATH = "./demos/matsim/single_intersection"
MATSIM_NETWORK_PATH = f"{PATH}/network_matsim.xml"
SUMO_NETWORK_PATH = f"{PATH}/network_sumo.xml"
MATSIM_POPULATION_PATH = f"{PATH}/population_matsim.xml"
SUMO_POPULATION_PATH = f"{PATH}/population_sumo.xml"
MATSIM_SIGNAL_CONTROL_PATH = f"{PATH}/signalSystems_matsim.xml"

MATSIM_NETWORK = ET.parse(MATSIM_NETWORK_PATH)
SUMO_NETWORK = ET.parse(SUMO_NETWORK_PATH)

START_TIME = dt.time(hour=6)            # Simulation start time
STEP_DURATION = dt.timedelta(seconds=10)  # Simulation step duration


def get_link_nodes(link_id: str) -> Tuple[ET.Element, ET.Element]:
    link = MATSIM_NETWORK.find(f'./links/link[@id="{link_id}"]')
    from_node_id = link.get('from')
    to_node_id = link.get('to')
    from_node = MATSIM_NETWORK.find(f'./nodes/node[@id="{from_node_id}"]')
    to_node = MATSIM_NETWORK.find(f'./nodes/node[@id="{to_node_id}"]')
    return from_node, to_node


def create_person(vehicle: ET.Element) -> ET.Element:
    vehicle_id = vehicle.get('id')
    vehicle_start_time = float(vehicle.get('depart'))
    vehicle_routes = vehicle.find('route').get('edges').split()
    from_node, _ = get_link_nodes(vehicle_routes[0])
    _, to_node = get_link_nodes(vehicle_routes[-1])
    end_time = (dt.datetime.combine(dt.date.today(), START_TIME) + STEP_DURATION * vehicle_start_time)

    person = ET.Element('person', {'id': str(vehicle_id)})
    plan = ET.Element('plan')
    start_activity = ET.Element('act', {
        'type': "home",
        'x': from_node.get('x'),
        'y': from_node.get('y'),
        # 'link': vehicle_routes[0],
        'end_time': end_time.strftime('%H:%M:%S')
    })
    leg = ET.Element('leg', {'mode': "car"})
    route = ET.Element('route')
    route.text = ' '.join(vehicle_routes)
    end_activity = ET.Element('act', {
        'type': "work",
        'x': to_node.get('x'),
        'y': to_node.get('y'),
        # 'link': vehicle_routes[-1]
    })

    leg.append(route)
    plan.append(start_activity)
    plan.append(leg)
    plan.append(end_activity)
    person.append(plan)
    return person


def create_signal_system(junction: ET.Element) -> ET.Element:
    junction_id = junction.get('id')
    junction_links = SUMO_NETWORK.findall(f'./connection[@tl="{junction_id}"]')
    unique_junction_liks_ids = set(l.get('from') for l in junction_links) | set(l.get('to') for l in junction_links)

    signal_system = ET.Element('signalSystem', {'id': f"SignalSystem_{junction_id}"})
    signals = ET.Element('signals')
    signals_list = [
        ET.Element('signal', {
            'linkIdRef': link_id,
            'id': f"Signal_{link_id}"
        }) for link_id in unique_junction_liks_ids
    ]

    signals.extend(signals_list)
    signal_system.append(signals)
    return signal_system


def create_population():
    input_tree = ET.parse(SUMO_POPULATION_PATH)
    output_tree = ET.Element('population')

    input_elements = input_tree.findall("./vehicle")
    output_elements = [create_person(v) for v in input_elements]

    output_tree.extend(output_elements)

    with open(MATSIM_POPULATION_PATH, 'wb') as f:
        f.writelines([
            '<?xml version="1.0" ?>'.encode('utf-8'),
            '<!DOCTYPE population SYSTEM "http://www.matsim.org/files/dtd/population_v5.dtd">'.encode('utf-8')
        ])
        ET.ElementTree(output_tree).write(f, 'utf-8')


def create_signal_systems():
    input_tree = ET.parse(SUMO_NETWORK_PATH)
    output_tree = ET.Element('signalSystems', {
        'xsi:schemaLocation': "http://www.matsim.org/files/dtd http://www.matsim.org/files/dtd/signalControl_v2.0.xsdhttp://www.matsim.org/files/dtd http://www.matsim.org/files/dtd/signalSystems_v2.0.xsd",
        'xmlns': "http://www.matsim.org/files/dtd",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance"
    })

    input_elements = input_tree.findall('./junction[@type="traffic_light"]')
    output_elements = [create_signal_system(s) for s in input_elements]

    output_tree.extend(output_elements)

    with open(MATSIM_SIGNAL_CONTROL_PATH, 'wb') as f:
        f.writelines([
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'.encode('utf-8')
        ])
        ET.ElementTree(output_tree).write(f, 'utf-8')


def main():
    create_population()
    create_signal_systems()


if __name__ == "__main__":
    main()
