import asyncio
from mcp import Client,StdioServerParameters


async def main():
    # Tell the client how to launch out server
    server=StdioServerParameters(
        command='python',
        args=['server.py']
    )

    # Connect to the server
    async with Client(server) as client:


        # Discover available tools
        tools=await client.list_tools()
        print("name",[tool.name for tool in tools.tools])

        # call the tools
        try:

            result= await client.call_tool(
                "add",
                {"a":5,"b":3}
            )
            if result.is_error:
                print("Tool Execution failed")
                for item in result.content:
                    if hasattr(item,"text"):
                        print(item.text)
            else:
                print(f"Result:",result.content)

        except Exception as e:
            print(f"Unexpected error :{type(e).__name__} :{e}")




        print(result)

        #resource
        resource=await client.read_resource("info:/calculator/about")
        print(resource)

        #prompt
        prompt=await client.get_prompt("explain_calculation",{"a":"10","b":"5"})
        print(prompt)


if __name__ =="__main__":
    asyncio.run(main())







