from poolseq.processing.gatk.index import Index
from poolseq.processing.gatk.haplotype_caller import HaplotypeCaller
from poolseq.processing.gatk.indel_realigner import IndelRealigner
from poolseq.processing.gatk.realigner_target_creator import RealignerTargetCreator


class Gatk():

    def __init__(self, data):
        self.index = Index(data)
        self.haplotype_caller = HaplotypeCaller(data)
        self.indel_realigner = IndelRealigner(data)
        self.realigner_target_creator = RealignerTargetCreator(data)
