from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    results = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            results[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename)
        )

    return results
