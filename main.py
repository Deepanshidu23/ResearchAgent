
import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load Environment Variables

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# TOOLS

def web_search(query):
    print(f"\n[WEB SEARCH] {query}")

    # Mock result
    return f"Prompt chaining is a workflow pattern where the output of one LLM call becomes the input of another."


def read_file(filename):
    print(f"\n[READ FILE] {filename}")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return str(e)


def write_file(filename, content):
    print(f"\n[WRITE FILE] {filename}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return "File written successfully"



# TOOL REGISTRY


TOOLS = {
    "web_search": web_search,
    "read_file": read_file,
    "write_file": write_file
}

# TOOL DEFINITIONS


tool_schemas = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search information on the internet",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file from disk",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string"
                    }
                },
                "required": ["filename"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": [
                    "filename",
                    "content"
                ]
            }
        }
    }
]


# USER TASK


messages = [
    {
        "role": "user",
        "content": "Research the Roadmap of Ai Engineering and save the summary into summary.txt"
    }
]


# AGENT LOOP


while True:

    print("\n" + "=" * 60)
    print("NEW AGENT ITERATION")
    print("=" * 60)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tool_schemas,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    print("\nASSISTANT RESPONSE:")
    print(assistant_message)

    messages.append(
        {
            "role": "assistant",
            "content": assistant_message.content or "",
            "tool_calls": assistant_message.tool_calls
        }
    )

    # Stop if no tool call exists
    if not assistant_message.tool_calls:

        print("\nFINAL ANSWER:")
        print(assistant_message.content)

        break

    # Execute Tool Calls
    for tool_call in assistant_message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        print(f"\nTOOL REQUESTED: {tool_name}")
        print(f"ARGUMENTS: {arguments}")

        tool_function = TOOLS[tool_name]

        result = tool_function(**arguments)

        print(f"\nTOOL RESULT:")
        print(result)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_name,
                "content": str(result)
            }
        )

print("\nAGENT FINISHED")