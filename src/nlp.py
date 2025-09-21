import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from agentic_functions import FUNCTION_DEFINITIONS
from model_instructions import SYSTEM_INSTRUCTIONS

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

tools = types.Tool(function_declarations=FUNCTION_DEFINITIONS)



config = types.GenerateContentConfig(
    tools=[tools],
    system_instruction=SYSTEM_INSTRUCTIONS
)

# ----------------------------
# Function call handler
# ----------------------------
def handle_function_call(func_name: str, func_args: dict, parser, console) -> str:
    """
    Map Gemini function calls to CommandParser commands.
    Returns captured output as a string.
    """
    output = ""

    if func_name == "list_directory":
        path = func_args.get("path", "")
        output = parser.execute(f"ls {path}".strip(), capture_output=True)

    elif func_name == "print_working_directory":
        output = parser.execute("pwd", capture_output=True)

    elif func_name == "change_directory":
        path = func_args.get("path", "")
        output = parser.execute(f"cd {path}", capture_output=True)

    elif func_name == "make_directory":
        path = func_args.get("path", "")
        output = parser.execute(f"mkdir {path}", capture_output=True)

    elif func_name == "cat_file":
        files = func_args.get("files", [])
        target = func_args.get("target")
        mode = func_args.get("mode", "read")
        content = func_args.get("content")

        args_str = " ".join(files)
        if target:
            if mode in ["write", "append"]:
                parser.execute(f"cat {args_str} {('>' if mode=='write' else '>>')} {target}", capture_output=True, content=content)
            else:
                parser.execute(f"cat {args_str}", capture_output=True)
        else:
            parser.execute(f"cat {args_str}", capture_output=True, content=content)

    elif func_name == "remove_path":
        path = func_args.get("path", "")
        output = parser.execute(f"rm {path}", capture_output=True)
    
    elif func_name == "move_path":
        source = func_args.get("source", "")
        destination = func_args.get("destination", "")
        parser.execute(f"mv {source} {destination}", capture_output=True)

    elif func_name == "show_cpu":
        output = parser.execute("cpu", capture_output=True)

    elif func_name == "show_memory":
        output = parser.execute("mem", capture_output=True)

    elif func_name == "list_processes":
        output = parser.execute("processes", capture_output=True)

    elif func_name == "show_help":
        output = parser.execute("help", capture_output=True)

    elif func_name == "exit_terminal":
        console.print(f"[magenta]Hope we meet again ^_^[/magenta]")
        console.print("[bold yellow]Exiting PyTerminal...[/bold yellow]")
        exit(1)

    else:
        output = f"[red]Function '{func_name}' is not implemented yet[/red]"

    return output


# ----------------------------
# NLP processing function
# ----------------------------
def process_nlp_input(user_text: str, parser, console):
    """
    Send user input to Gemini.
    - If Gemini returns a function call, execute it via handle_function_call.
    - Then append the function result back to Gemini to get a final response.
    - If no function call, just print Gemini's response.
    """
    try:
        # Initial request
        contents = [types.Content(role="user", parts=[types.Part(text=user_text)])]
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            config=config
        )
    except Exception as e:
        console.print(f"[red]Error calling Gemini API: {e}[/red]")
        return

    candidate = response.candidates[0]
    part = candidate.content.parts[0]

    if part.function_call:
        func_name = part.function_call.name
        args = part.function_call.args

        # Capture function output
        result = handle_function_call(func_name, args, parser, console)

        # Create function response part
        function_response_part = types.Part.from_function_response(
            name=func_name,
            response={"result": result}
        )

        # Append the original response + function result for final output
        contents.append(candidate.content)  # original model content
        contents.append(types.Content(role="function", parts=[function_response_part]))

        # Get final response from Gemini
        final_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            config=config
        )

        console.print(f"[magenta]{final_response.text}[/magenta]")

    else:
        # No function call; just print text
        console.print(f"[magenta]{part.text}[/magenta]")
