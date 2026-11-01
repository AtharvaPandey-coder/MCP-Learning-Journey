from mcp.server.mcpserver import MCPServer
#from mcp.server.mcpserver.resources.base import Resource
## Create an mcp sever 
mcp=MCPServer("my claculator")

#3 Register an python fuynction as an mcp tool
@mcp.tool()
def add(a:int,b:int)-> int:
    """Add two numbers and add the result"""

    if not isinstance(a,int) or isinstance(a,bool):
        raise ValueError("Fist input must be a string")

    if not isinstance(b,int) or isinstance(b,bool):
        raise ValueError("Second input must be a string")

    if abs(a) > 1000000 or abs(b) > 1000000:
        raise ValueError("Number must be within the allowed range")

    
    return a + b 



@mcp.tool()
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a *b

@mcp.resource(uri="info:/calculator/about",name="Calculator Information",description="Information baout the calculator server",mime_type="text/plain",)
def calculator_info() -> str:
    """Returns Information about this calculator"""
    return (
        "Calculator MCP Server\n"
        "Available tools:\n"
        "- add: Adds two numbers\n"
        "- multiply: Multiplies two numbers\n"
    )

@mcp.prompt()
def explain_calculation(a:int,b:int) ->str:
    """Generate instructions for explaining an calculations"""
    return(
        f"Explain the addition of {a} and {b} step by step. "
        f"Calculate {a} + {b} and explain the result simply."
    )

#start the server
if __name__ == "__main__" :
    mcp.run()










