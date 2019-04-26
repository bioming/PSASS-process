from collections import OrderedDict
from poolsex.data.variables import variables
from poolsex.data import module_commands as commands


def get_modules_info():
    '''
    All the information about each module is defined in this function:
    - prefix: prefix of the shell file / output file / job name
    - clean_temp: files should be removed if "clean_temp" option is on ()
    - results_format: format of
    - sex: separate sexes (T/F)
    - lane: separate lane (T/F)
    - mate: separate mates (T/F)
    - pairwise: run for each pair of file (T/F)
    - options: scheduler options (memory, threads ...)
    The function returns a dictionary giving the information about each module.
    '''

    modules = OrderedDict([(variables.modules.index, {variables.modules_options.prefix: 'index',
                                                      variables.modules_options.clean_temp: False,
                                                      variables.modules_options.results_format: None,
                                                      variables.modules_options.sex: False,
                                                      variables.modules_options.lane: False,
                                                      variables.modules_options.mate: False,
                                                      variables.modules_options.pairwise: False,
                                                      variables.modules_options.options: [variables.submit_options.name,
                                                                                          variables.submit_options.mem,
                                                                                          variables.submit_options.output,
                                                                                          variables.submit_options.error],
                                                      variables.modules_options.dependencies: None,
                                                      variables.modules_options.command: commands.index
                                                      }),

                           (variables.modules.mapping, {variables.modules_options.prefix: 'mapping',
                                                        variables.modules_options.clean_temp: True,
                                                        variables.modules_options.results_format: 'bam',
                                                        variables.modules_options.sex: True,
                                                        variables.modules_options.lane: True,
                                                        variables.modules_options.mate: True,
                                                        variables.modules_options.pairwise: False,
                                                        variables.modules_options.options: [variables.submit_options.name,
                                                                                            variables.submit_options.threads,
                                                                                            variables.submit_options.output,
                                                                                            variables.submit_options.error],
                                                        variables.modules_options.dependencies: variables.modules.index,
                                                        variables.modules_options.command: commands.mapping
                                                        }),

                           (variables.modules.sort, {variables.modules_options.prefix: 'sort',
                                                     variables.modules_options.clean_temp: True,
                                                     variables.modules_options.results_format: 'bam',
                                                     variables.modules_options.sex: True,
                                                     variables.modules_options.lane: True,
                                                     variables.modules_options.mate: False,
                                                     variables.modules_options.pairwise: False,
                                                     variables.modules_options.options: [variables.submit_options.name,
                                                                                         variables.submit_options.mem,
                                                                                         variables.submit_options.h_vmem,
                                                                                         variables.submit_options.output,
                                                                                         variables.submit_options.error],
                                                     variables.modules_options.dependencies: variables.modules.mapping,
                                                     variables.modules_options.command: commands.sort
                                                     }),

                           (variables.modules.groups, {variables.modules_options.prefix: 'groups',
                                                       variables.modules_options.clean_temp: True,
                                                       variables.modules_options.results_format: 'bam',
                                                       variables.modules_options.sex: True,
                                                       variables.modules_options.lane: True,
                                                       variables.modules_options.mate: False,
                                                       variables.modules_options.pairwise: False,
                                                       variables.modules_options.options: [variables.submit_options.name,
                                                                                           variables.submit_options.mem,
                                                                                           variables.submit_options.h_vmem,
                                                                                           variables.submit_options.output,
                                                                                           variables.submit_options.error],
                                                       variables.modules_options.dependencies: variables.modules.sort,
                                                       variables.modules_options.command: commands.groups
                                                       }),

                           (variables.modules.merge, {variables.modules_options.prefix: 'merge',
                                                      variables.modules_options.clean_temp: True,
                                                      variables.modules_options.results_format: 'bam',
                                                      variables.modules_options.sex: True,
                                                      variables.modules_options.lane: False,
                                                      variables.modules_options.mate: False,
                                                      variables.modules_options.pairwise: False,
                                                      variables.modules_options.options: [variables.submit_options.name,
                                                                                          variables.submit_options.mem,
                                                                                          variables.submit_options.h_vmem,
                                                                                          variables.submit_options.output,
                                                                                          variables.submit_options.error],
                                                      variables.modules_options.dependencies: variables.modules.groups,
                                                      variables.modules_options.command: commands.merge
                                                      }),

                           (variables.modules.duplicates, {variables.modules_options.prefix: 'duplicates',
                                                           variables.modules_options.clean_temp: False,
                                                           variables.modules_options.results_format: 'bam',
                                                           variables.modules_options.sex: True,
                                                           variables.modules_options.lane: False,
                                                           variables.modules_options.mate: False,
                                                           variables.modules_options.pairwise: False,
                                                           variables.modules_options.options: [variables.submit_options.name,
                                                                                               variables.submit_options.mem,
                                                                                               variables.submit_options.h_vmem,
                                                                                               variables.submit_options.output,
                                                                                               variables.submit_options.error],
                                                           variables.modules_options.dependencies: variables.modules.merge,
                                                           variables.modules_options.command: commands.duplicates
                                                           }),

                           (variables.modules.mpileup, {variables.modules_options.prefix: 'mpileup',
                                                        variables.modules_options.clean_temp: True,
                                                        variables.modules_options.results_format: 'pileup',
                                                        variables.modules_options.sex: False,
                                                        variables.modules_options.lane: False,
                                                        variables.modules_options.mate: False,
                                                        variables.modules_options.pairwise: True,
                                                        variables.modules_options.options: [variables.submit_options.name,
                                                                                            variables.submit_options.threads,
                                                                                            variables.submit_options.output,
                                                                                            variables.submit_options.error],
                                                        variables.modules_options.dependencies: variables.modules.duplicates,
                                                        variables.modules_options.command: commands.mpileup
                                                        }),

                           (variables.modules.mpileup2sync, {variables.modules_options.prefix: 'mpileup2sync',
                                                             variables.modules_options.clean_temp: False,
                                                             variables.modules_options.results_format: 'sync',
                                                             variables.modules_options.sex: False,
                                                             variables.modules_options.lane: False,
                                                             variables.modules_options.mate: False,
                                                             variables.modules_options.pairwise: True,
                                                             variables.modules_options.options: [variables.submit_options.name,
                                                                                                 variables.submit_options. threads,
                                                                                                 variables.submit_options.output,
                                                                                                 variables.submit_options.error],
                                                             variables.modules_options.dependencies: variables.modules.mpileup,
                                                             variables.modules_options.command: commands.mpileup2sync
                                                             }),

                           (variables.modules.clean_temp, {variables.modules_options.prefix: 'clean_temp',
                                                           variables.modules_options.clean_temp: False,
                                                           variables.modules_options.results_format: None,
                                                           variables.modules_options.sex: False,
                                                           variables.modules_options.lane: False,
                                                           variables.modules_options.mate: False,
                                                           variables.modules_options.pairwise: False,
                                                           variables.modules_options.options: [variables.submit_options.name,
                                                                                               variables.submit_options.output,
                                                                                               variables.submit_options.error],
                                                           variables.modules_options.dependencies: variables.modules.mpileup2sync,
                                                           variables.modules_options.command: commands.clean_temp
                                                           })]
                          )

    return modules
