from aiohttp.test_utils import AioHTTPTestCase

from main import app


class TestPaymentGateway(AioHTTPTestCase):

    async def get_application(self):
        return app

    async def test_handle_payment(self):
        # Prepare the request data
        data = {"amount": 100}

        # Make a POST request to the /charge endpoint
        resp = await self.client.post("/charge", json=data)

        # Assert the response status is 200
        assert resp.status == 200

        # Assert the response json is {"status": "success"}
        json_data = await resp.json()
        assert json_data == {"status": "success"}