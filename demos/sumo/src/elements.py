import xml.etree.ElementTree as ET

from pathlib import Path


class Junction:
    def __init__(self, junction_id: str):
        self.id = junction_id 
        self.phases = None 
        self._connections = None

    @property
    def connections(self):
        return self._connections

    @connections.setter 
    def connections(self, connects: list):
        self._connections = sorted(connects, key=lambda x: x.index)


class Phase:
    def __init__(self, state: str):
        self.state = state
        self.allowed_indices = [
            i for i, signal in enumerate(list(self.state.lower())) if signal == 'g'
        ]


class Connection:
    def __init__(self, index: int, from_lane: str, to_lane: str):
        self.index = index 
        self.from_lane = from_lane 
        self.to_lane = to_lane


def read_from_net_xml(path: Path):
    tree = ET.parse(path)

    junctions = dict()
    phases = dict() 
    connections = dict()

    for child in tree.getroot():
        tag = child.tag 
        attrib = child.attrib

        if tag == 'tlLogic':
            junction_id = attrib['id']
            phases[junction_id] = (
                [Phase(phase.attrib['state']) for phase in child] 
            )

        elif tag == 'junction' and attrib['type'] == 'traffic_light':
            junction_id = attrib['id']
            junctions[junction_id] = Junction(junction_id)

        elif tag == 'connection' and 'tl' in attrib.keys():
            junction_id = attrib['tl']
            if junction_id not in connections:
                connections[junction_id] = []

            from_lane_index = f'{attrib["from"]}_{attrib["fromLane"]}'
            to_lane_index = f'{attrib["to"]}_{attrib["toLane"]}'

            connections[junction_id].append(
                Connection(
                    int(attrib["linkIndex"]), 
                    from_lane_index,
                    to_lane_index)
            )

    for junction_id, junction in junctions.items():
        junction.phases = phases[junction_id]
        junction.connections = connections[junction_id]

    return junctions


if __name__ == '__main__':
    junctions = read_from_net_xml(Path('demos/sumo/single_intersection.net.xml'))
    junction = list(junctions.items())[0][1]
    for phase in junction.phases:
        print(phase.state, phase.allowed_indices)
    for connection in junction.connections:
        print(connection.index, connection.from_lane, connection.to_lane)