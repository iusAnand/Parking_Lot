class GateRepo:
    gate_map = {}

    def __init__(self):
        self.gate_map = {}  # gate_id to Gate object mapping


    def find_gate_by_id(self, gate_id):
        if gate_id in self.gate_map:
            return self.gate_map[gate_id]
        return None

    