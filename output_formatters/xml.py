from dicttoxml import dicttoxml


def format_output(results):
    for result in results:
        del result['confidence']

    return dicttoxml(results, custom_root='results', attr_type=False)
