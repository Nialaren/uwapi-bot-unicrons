class Constructions:
    def __init__(self):
        self._protoDict: dict[str, int] = {}
        self.initialized = False

    def init(self, data: dict[str, int]):
        self._protoDict = data
        self.initialized = True

    @property
    def experimental_assembler(self):
        return self._protoDict['experimental_assembler']
    @property
    def brick(self):
        return self._protoDict['brick']
    @property
    def drill(self):
        return self._protoDict['drill']
    @property
    def talos(self):
        return self._protoDict['talos']
    @property
    def forgepress(self):
        return self._protoDict['forgepress']
    @property
    def pump(self):
        return self._protoDict['pump']
    @property
    def laboratory(self):
        return self._protoDict['laboratory']
    @property
    def vehicle_assembler(self):
        return self._protoDict['vehicle_assembler']
    @property
    def generator(self):
        return self._protoDict['generator']
    @property
    def factory(self):
        return self._protoDict['factory']
    @property
    def blender(self):
        return self._protoDict['blender']
    @property
    def heimdall(self):
        return self._protoDict['heimdall']
    @property
    def arsenal(self):
        return self._protoDict['arsenal']
    @property
    def smelter(self):
        return self._protoDict['smelter']
    @property
    def bot_assembler(self):
        return self._protoDict['bot_assembler']
    @property
    def concrete_plant(self):
        return self._protoDict['concrete_plant']
    @property
    def thor(self):
        return self._protoDict['thor']

    def is_initialized(self):
        return self.initialized

class Recipes:
    def __init__(self):
        self._protoDict: dict[str, int] = {}
        self.initialized = False

    def init(self, data: dict[str, int]):
        self._protoDict = data
        self.initialized = True

    @property
    def plasma_emitter(self):
        return self._protoDict['plasma_emitter']
    @property
    def mermaid(self):
        return self._protoDict['mermaid']
    @property
    def eagle(self):
        return self._protoDict['eagle']
    @property
    def ATV(self):
        return self._protoDict['ATV']
    @property
    def rail_gun(self):
        return self._protoDict['rail_gun']
    @property
    def aether(self):
        return self._protoDict['aether']
    @property
    def lurker(self):
        return self._protoDict['lurker']
    @property
    def armor_plates(self):
        return self._protoDict['armor_plates']
    @property
    def oil(self):
        return self._protoDict['oil']
    @property
    def kitsune(self):
        return self._protoDict['kitsune']
    @property
    def twinfire(self):
        return self._protoDict['twinfire']
    @property
    def atomic_forge(self):
        return self._protoDict['atomic_forge']
    @property
    def power_cell(self):
        return self._protoDict['power_cell']
    @property
    def reinforced_plates(self):
        return self._protoDict['reinforced_plates']
    @property
    def golem(self):
        return self._protoDict['golem']
    @property
    def paladin(self):
        return self._protoDict['paladin']
    @property
    def reinforced_concrete(self):
        return self._protoDict['reinforced_concrete']
    @property
    def alloys(self):
        return self._protoDict['alloys']
    @property
    def juggernaut(self):
        return self._protoDict['juggernaut']
    @property
    def quantum_ray(self):
        return self._protoDict['quantum_ray']
    @property
    def cyclops(self):
        return self._protoDict['cyclops']
    @property
    def shield_projector(self):
        return self._protoDict['shield_projector']
    @property
    def crystals(self):
        return self._protoDict['crystals']
    @property
    def blaster(self):
        return self._protoDict['blaster']
    @property
    def colossus(self):
        return self._protoDict['colossus']
    @property
    def quark_foam(self):
        return self._protoDict['quark_foam']
    @property
    def metal(self):
        return self._protoDict['metal']

    def is_initialized(self):
        return self.initialized

class ConstructionUnit:
    def __init__(self):
        self._protoDict: dict[str, int] = {}
        self.initialized = False

    def init(self, data: dict[str, int]):
        self._protoDict = data
        self.initialized = True

    @property
    def experimental_assembler(self):
        return self._protoDict['experimental_assembler']
    @property
    def brick(self):
        return self._protoDict['brick']
    @property
    def drill(self):
        return self._protoDict['drill']
    @property
    def talos(self):
        return self._protoDict['talos']
    @property
    def forgepress(self):
        return self._protoDict['forgepress']
    @property
    def pump(self):
        return self._protoDict['pump']
    @property
    def laboratory(self):
        return self._protoDict['laboratory']
    @property
    def vehicle_assembler(self):
        return self._protoDict['vehicle_assembler']
    @property
    def generator(self):
        return self._protoDict['generator']
    @property
    def factory(self):
        return self._protoDict['factory']
    @property
    def blender(self):
        return self._protoDict['blender']
    @property
    def heimdall(self):
        return self._protoDict['heimdall']
    @property
    def arsenal(self):
        return self._protoDict['arsenal']
    @property
    def smelter(self):
        return self._protoDict['smelter']
    @property
    def bot_assembler(self):
        return self._protoDict['bot_assembler']
    @property
    def concrete_plant(self):
        return self._protoDict['concrete_plant']
    @property
    def thor(self):
        return self._protoDict['thor']

    def is_initialized(self):
        return self.initialized


class Units:
    def __init__(self):
        self._protoDict: dict[str, int] = {}
        self.initialized = False

    def init(self, data: dict[str, int]):
        self._protoDict = data
        self.initialized = True

    def is_initialized(self):
        return self.initialized
    
    @property
    def plasma_emitter(self):
        return self._protoDict['plasma_emitter']

    @property
    def mermaid(self):
        return self._protoDict['mermaid']

    @property
    def eagle(self):
        return self._protoDict['eagle']

    @property
    def ATV(self):
        return self._protoDict['ATV']

    @property
    def lurker(self):
        return self._protoDict['lurker']
    
    @property
    def kitsune(self):
        return self._protoDict['kitsune']

    @property
    def twinfire(self):
        return self._protoDict['twinfire']

    @property
    def golem(self):
        return self._protoDict['golem']

    @property
    def paladin(self):
        return self._protoDict['paladin']

    @property
    def juggernaut(self):
        return self._protoDict['juggernaut']

    @property
    def cyclops(self):
        return self._protoDict['cyclops']

    @property
    def colossus(self):
        return self._protoDict['colossus']
    
class Resources:
    def __init__(self):
        self._protoDict: dict[str, int] = {}
        self.initialized = False

    def init(self, data: dict[str, int]):
        self._protoDict = data
        self.initialized = True

    def is_initialized(self):
        return self.initialized
    
    @property
    def metal(self):
        return self._protoDict['metal']

    @property
    def aether(self):
        return self._protoDict['aether']

    @property
    def oil(self):
        return self._protoDict['oil']

    @property
    def crystals(self):
        return self._protoDict['crystals']

def get_construction_to_unit_map(constructions: Constructions, units: ConstructionUnit) -> dict[int, int]:
    return {
        constructions.experimental_assembler: units.experimental_assembler,
        constructions.brick: units.brick,
        constructions.drill: units.drill,
        constructions.talos: units.talos,
        constructions.forgepress: units.forgepress,
        constructions.pump: units.pump,
        constructions.laboratory: units.laboratory,
        constructions.vehicle_assembler: units.vehicle_assembler,
        constructions.generator: units.generator,
        constructions.factory: units.factory,
        constructions.blender: units.blender,
        constructions.heimdall: units.heimdall,
        constructions.arsenal: units.arsenal,
        constructions.smelter: units.smelter,
        constructions.bot_assembler: units.bot_assembler,
        constructions.concrete_plant: units.concrete_plant,
        constructions.thor: units.thor,
    }
    
def get_unit_to_construction_map(constructions: Constructions, units: ConstructionUnit) -> dict[int, int]:
    return {
        units.experimental_assembler: constructions.experimental_assembler,
        units.brick: constructions.brick,
        units.drill: constructions.drill,
        units.talos: constructions.talos,
        units.forgepress: constructions.forgepress,
        units.pump: constructions.pump,
        units.laboratory: constructions.laboratory,
        units.vehicle_assembler: constructions.vehicle_assembler,
        units.generator: constructions.generator,
        units.factory: constructions.factory,
        units.blender: constructions.blender,
        units.heimdall: constructions.heimdall,
        units.arsenal: constructions.arsenal,
        units.smelter: constructions.smelter,
        units.bot_assembler: constructions.bot_assembler,
        units.concrete_plant: constructions.concrete_plant,
        units.thor: constructions.thor,
    }