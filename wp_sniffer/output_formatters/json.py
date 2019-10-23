import json


def format_output(results):
    for result in results:
        del result['confidence']

    return json.dumps(results)
