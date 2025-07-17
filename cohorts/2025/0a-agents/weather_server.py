import random
from fastmcp import FastMCP


known_weather_data = {
    'berlin': 20.0
}


# FastMCP is a Python library for building multi-agent conversational platforms (MCPs).
# It allows you to create, manage, and orchestrate multiple AI agents that can interact with each other and users in real time.
# FastMCP provides tools for agent communication, memory, and workflow management, making it easier to develop complex conversational systems.
mcp = FastMCP("Demo 🚀")


@mcp.tool  # Registers get_weather as a callable tool for agents.
def get_weather(city: str) -> float:
    """Get the current weather for a given city or location."""

    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]

    return round(random.uniform(-5, 35), 1)


@mcp.tool  # Registers set_weather as a callable tool for agents.
def set_weather(city: str, temp: float) -> None:
    """this function sets or updates the temperature for a city or location."""
    """needs the city name and the temperature in Celsius"""

    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a number.")

    city = city.strip().lower()
    known_weather_data[city] = temp  # Update the temperature for a given city
    return 'OK'


if __name__ == "__main__":
    mcp.run()   # start the MCP server and waits for agents/clients to connect
