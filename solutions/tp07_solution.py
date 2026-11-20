import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from common.config import get_model

async def main():
    client = MultiServerMCPClient({
        "dojo": {
            "transport": "stdio",
            "command": "python",
            "args": ["-m", "tp07_mcp.server"]
        }
    })
    tools = await client.get_tools()
    agent = create_agent(
        model=get_model(), tools=tools,
        system_prompt="Tu es un assistant RH de démonstration. Les données sont fictives."
    )
    result = await agent.ainvoke({
        "messages": [{"role": "user", "content":
            "Quelles formations fictives sont disponibles sur Kubernetes ?"}]
    })
    print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
