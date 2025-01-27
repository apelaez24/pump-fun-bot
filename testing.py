import asyncio
import websockets
import base64

# WebSocket endpoint with authentication
WSS_ENDPOINT = "wss://solana-mainnet.core.chainstack.com/b853b9fe04dc8306289250d"

# Replace with your actual username and password
USERNAME = "xenodochial-bhaskara"
PASSWORD = "repent-outing-hassle-cache-scorn-cradle"

# Generate Base64-encoded credentials for Basic Authentication
credentials = f"{USERNAME}:{PASSWORD}"
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

async def test_wss():
    try:
        # Add the Authorization header
        async with websockets.connect(
            WSS_ENDPOINT,
            extra_headers={"Authorization": f"Basic {encoded_credentials}"}
        ) as websocket:
            print("WebSocket connection successful!")
    except Exception as e:
        print(f"Failed to connect to WebSocket: {e}")

# Run the WebSocket test
asyncio.run(test_wss())
