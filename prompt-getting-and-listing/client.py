import asyncio
from fastmcp import Client
from rich import print

client = Client("http://127.0.0.1:8000/sse")

async def main():
    async with client:
        
        # wrong way to call the prompt, will raise an error
        # about_topic = await client.get_prompt("ask_about_topic", topic="quantum computing")

        # correct way to call the prompt, passing the arguments as a dictionary
        about_topic = await client.get_prompt("ask_about_topic", {"topic":"quantum computing"})

        print("*" * 80, sep="\n")
        print(f"About Topic: {about_topic}")
        print("*" * 80, sep="\n")

        print("About Topic: ", about_topic)
        print("*" * 80, sep="\n")

        code_request = await client.get_prompt("generate_code_request", {"language": "Python", "task_description": "sort a list of numbers"})
        print (code_request)
        print("*" * 80, sep="\n")

        for message in code_request.messages:
            print(f"Prompt Structure [Role : {message.role}] \n Content : {message.content}")
            print("*" * 80, sep="\n")


        for message in code_request.messages:
            print(f"""
                [Role : {message.role}]
                Content : {message.content.text}
                """)
            print("*" * 80, sep="\n")

        all_prompts = await client.list_prompts()
        print("All Prompts: ", all_prompts)


if __name__ == "__main__":
    asyncio.run(main())
