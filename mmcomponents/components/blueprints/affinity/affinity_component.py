from mmcomponents.models.components.docking.output import DockingOutput
from mmcomponents.models.components.affinity.output import AffinityOutput
from mmcomponents.base.base_component import ProgramHarness

class DockingAffinityComponent(ProgramHarness):
    
    @classmethod
    def input(cls):
        return DockingOutput

    @classmethod
    def output(cls):
        return AffinityOutput