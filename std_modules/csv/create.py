    for x in csv.reader(data,
                        delimiter=':',
                        escapechar='\\',
                        quotechar='\x00',
                        doublequote=False,
                        skipinitialspace=False,
                        lineterminator=os.linesep,
                        quoting=csv.QUOTE_NONE,
                        ) if x and not x[0].startswith('#')
]