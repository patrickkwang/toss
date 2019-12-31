"""Setup TOS server."""
from jinja2 import Environment, PackageLoader
from sanic import Sanic, response

env = Environment(
    loader=PackageLoader('toss', 'templates')
)
template = env.get_template('terms.txt')

app = Sanic()
app.config.ACCESS_LOG = False


@app.route('/tos')
async def tos(request):
    """Get terms of service."""
    if 'service_long' not in request.args:
        return response.text('"service_long" is a required query parameter', status=400)
    if 'provider_long' not in request.args:
        return response.text('"provider_long" is a required query parameter', status=400)
    args = {
        'service': {
            'long': request.args.get('service_long'),
            'short': request.args.get('service_short', 'the Service'),
        },
        'provider': {
            'long': request.args.get('provider_long'),
            'short': request.args.get('provider_short', 'the Provider'),
        },
    }
    return response.text(template.render(**args))
