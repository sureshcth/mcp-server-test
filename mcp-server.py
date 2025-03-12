from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Analytics Server")

# Add tools AI can call


@mcp.tool()
def calculate_metric(value1: float, value2: float) -> float:
    """Calculate an important metric"""
    return value1 * value2 / 100


# Expose data as resources
@mcp.resource("docs://{document_id}")
def get_document(document_id: str) -> str:
    """Get document content"""
    return f"Content for document {document_id}"

# Define standard prompts


@mcp.prompt()
def analyze_data() -> str:
    """Guide AI data analysis"""
    return "Please analyze this data following company guidelines..."


# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
