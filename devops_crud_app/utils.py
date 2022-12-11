def render_response_example(example: dict) -> dict:
    return {
        'content': {
            'application/json': {
                'example': example
            }
        }
    }