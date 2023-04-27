import asyncio
import random
from aiocoap import Context, Message, Code

async def main():
    # Bind to port 5684 for outgoing requests
    client_address = ('', 5684)
    context = await Context.create_client_context(local_addr=client_address)

    while True:
        # Generate randomized temperature data
        temperature_data = random.uniform(-50, 50)
        payload = str(temperature_data).encode("utf-8")

        # Send the data to the server
        request = Message(code=Code.POST, payload=payload, uri="coap://localhost/temperature")
        response = await context.request(request).response

        print(f"Sent temperature data: {temperature_data}, received response: {response.code}")

        await asyncio.sleep(5)  # Adjust the interval between sending data as needed

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())