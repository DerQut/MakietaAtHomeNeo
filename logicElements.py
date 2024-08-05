class Gate:
    def __init__(self, maxInputs: int, isNegated=False):
        self.maxInputs = maxInputs
        self.inputs: [Gate] = []

        while len(self.inputs) < self.maxInputs:
            self.inputs.append(None)

        self.internalState = False
        self.externalState = False
        self.isNegated = isNegated

    def calculateInternalState(self):
        ...

    def sendExternalState(self):
        self.externalState = self.internalState ^ self.isNegated


class AndGate(Gate):
    def calculateInternalState(self):

        if self.inputs == [None] * self.maxInputs:
            self.internalState = False
            return -1

        for gate in self.inputs:
            if isinstance(gate, Gate) and not gate.externalState:
                self.internalState = False
                return 0

        self.internalState = True
        return 1


class OrGate(Gate):
    def calculateInternalState(self):
        self.internalState = False
        for gate in self.inputs:
            if isinstance(gate, Gate) and gate.externalState:
                self.internalState = True
                return 1
        return 0


class Buffer(Gate):
    def __init__(self, isNegated=False):
        super().__init__(1, isNegated)

    def calculateInternalState(self):
        self.internalState = False
        if self.inputs == [None]:
            return -1

        if self.inputs[0].externalState:
            self.internalState = True
            return 1
        return 0
