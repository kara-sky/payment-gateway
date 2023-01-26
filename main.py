from aiohttp import web

from config import PaymentGatewayConfig

config = PaymentGatewayConfig()

async def handle_payment(request):
    json_data = await request.json()
    print(json_data)
    return web.json_response({"status": "success"})

app = web.Application()
app.add_routes([web.post('/charge', handle_payment)])

if __name__ == '__main__':
    web.run_app(app, port=config.port)
