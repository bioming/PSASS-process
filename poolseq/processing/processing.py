import os
from collections import defaultdict
from poolseq.processing.bwa import Bwa
from poolseq.processing.picard import Picard
from poolseq.processing.gatk import Gatk


class Processing():

    def __init__(self, data):
        self.bwa = Bwa(data)
        self.picard = Picard(data)
        self.gatk = Gatk(data)
        self.files_info = self.get_files_info(data)

    def generate_shell_files(self, data, parameters):
        self.bwa.index.generate_files(data, parameters)
        files_info = self.files_info
        for sex, lanes in files_info.items():
            for lane, mates in lanes.items():
                self.bwa.mapping.generate_shell_files(data,
                                                      parameters,
                                                      sex,
                                                      lane,
                                                      mates)
                self.picard.sort.generate_shell_files(data,
                                                      parameters,
                                                      sex,
                                                      lane)
                self.picard.add_read_groups.generate_shell_files(data,
                                                                 parameters,
                                                                 sex,
                                                                 lane)
                self.picard.merge.generate_shell_files(data,
                                                       parameters,
                                                       sex,
                                                       lane)

    def get_files_info(self, data):
        files_info = defaultdict(lambda: defaultdict(lambda: list()))
        for file in data.reads_paths:
            dir_path, file_name = os.path.split(file)
            file_name = file_name.replace('.fastq.gz', '')
            fields = file_name.split('_')
            sex = fields[0]
            lane = fields[1]
            mate = fields[2]
            files_info[sex][lane].append(mate)
        return files_info
