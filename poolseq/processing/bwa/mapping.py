import os
import poolseq.genotoul as genotoul
from poolseq.processing import file_utils


class Mapping():

    def __init__(self, data):
        self.qsub_file_path = os.path.join(data.directories.qsub, 'mapping.sh')
        self.shell_file_path = []
        self.output_file_path = []

    def generate_shell_files(self, data, parameters, sex, lane, mates):
        qsub_file = file_utils.wa_open(self.qsub_file_path)
        base_file_name = '_'.join([sex, lane])
        base_shell_name = 'mapping_' + base_file_name
        shell_file_path = os.path.join(data.directories.shell, base_shell_name + '.sh')
        shell_file = open(shell_file_path, 'w')
        output_file_path = os.path.join(data.directories.output, base_file_name + '.bam')
        r1_file_path = os.path.join(data.directories.reads,
                                    base_file_name + '_' + mates[0] + '.fastq.gz')
        r2_file_path = os.path.join(data.directories.reads,
                                    base_file_name + '_' + mates[1] + '.fastq.gz')
        genotoul.print_header(shell_file,
                              name=base_shell_name,
                              threads=parameters.threads)
        shell_file.write(parameters.bwa + ' mem' +
                         ' -t ' + str(parameters.threads) +
                         ' ' + data.genome_path +
                         ' ' + r1_file_path +
                         ' ' + r2_file_path +
                         ' | samtools view -b -' +
                         ' > ' + output_file_path + '\n')
        shell_file.close()
        self.shell_file_path.append(shell_file_path)
        self.output_file_path.append(output_file_path)
        qsub_file.write('qsub ' + shell_file_path + '\n')
        qsub_file.close()
