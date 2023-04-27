import asyncio
from aiocoap import resource, Context, Message
from aiocoap.numbers.codes import Code

class TemperatureResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.add_param(resource.Resource.Param("title", "Temperature Data Receiver"))

    async def render_post(self, request):
        temperature_data = request.payload.decode("utf-8")
        print(f"Received temperature data: {temperature_data}")
        return Message(code=Code.CHANGED)  # Send acknowledgment

def main():
    root = resource.Site()
    root.add_resource(('temperature',), TemperatureResource())

    server_address = ('', 5683)  # Use port 5683
    asyncio.Task(Context.create_server_context(root, bind=server_address))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()