import ast
import traceback
import pdb

# Extended dictionary with potential fixes
ERROR_DICT = {
    "ZeroDivisionError": {
        "explanation": "Occurs when dividing by zero.",
        "fix": "Check that the denominator is not zero before dividing.",
    },
    "IndexError": {
        "explanation": "Happens when accessing an index outside a sequence’s valid range.",
        "fix": "Check list/array bounds before accessing. Or use len().",
    },
    "KeyError": {
        "explanation": "Accessing a dictionary key that does not exist.",
        "fix": "Ensure the key is valid or handle missing keys using dict.get(key).",
    },
    "TypeError": {
        "explanation": "Operation applied to object of incompatible type.",
        "fix": "Check variable types or cast/convert them to the correct type.",
    },
    "ValueError": {
        "explanation": "Argument is correct type but invalid value.",
        "fix": "Validate data values or handle them with exception blocks.",
    },
    "SyntaxError": {
        "explanation": "Malformed Python code (e.g., missing colons or parentheses).",
        "fix": "Check Python syntax, colons, indentation, parentheses, or quotes.",
    },
}

def minimal_patch_suggestion(code_line: str, error_type: str) -> str:
    """
    Provide a simple patch snippet based on the line of code that triggered an error.
    Currently very naive; add your own heuristics or fancy logic here!
    """
    if error_type == "ZeroDivisionError" and "/" in code_line:
        return f"Try:  if denominator != 0:\n    {code_line}\nelse:\n    # Handle zero denominator"
    if error_type == "KeyError" and "[" in code_line:
        return f"Try using get:  my_dict.get('missingKey', default_value)"
    # Otherwise, just return a generic suggestion
    return "No specific patch suggestion available."

def syntax_check(code: str) -> str:
    """
    Returns an empty string if syntax is valid, or a syntax error message if not.
    """
    try:
        ast.parse(code)
        return ""
    except SyntaxError as e:
        return f"SyntaxError: {str(e)}"

def debug_code(code: str, interactive: bool = False) -> str:
    """
    1. Checks syntax with AST.
    2. Executes code if syntax is okay.
    3. If an error occurs, returns a plain‑language explanation & minimal fix suggestions.
    4. Optionally offers post‑mortem debugging if interactive = True.
    """

    # Attempt to parse code
    syntax_err = syntax_check(code)
    if syntax_err:
        return f"Syntax Error Detected:\n{syntax_err}\n\nExplanation:\n{ERROR_DICT['SyntaxError']['explanation']}\nSuggested Fix:\n{ERROR_DICT['SyntaxError']['fix']}"

    # Attempt to run code
    try:
        # Remove non-ascii if needed
        safe_code = code.encode('ascii', 'ignore').decode('ascii')
        exec(safe_code, {})
        return "No errors found."
    except Exception as e:
        tb_str = traceback.format_exc()
        # Last line of the traceback shows the error type
        last_line = tb_str.strip().split("\n")[-1]
        error_type = last_line.split(":")[0]
        details = ERROR_DICT.get(error_type, {"explanation": "No explanation available.", "fix": "No suggested fix."})
        
        # Attempt to extract the line that caused the error
        # (very naive approach: look for 'File "<string>", line ...')
        error_line = "Unknown"
        for line in tb_str.split("\n"):
            if 'File "<string>", line ' in line:
                error_line = line.strip()
                break
        
        # Provide minimal patch suggestion if possible
        patch = minimal_patch_suggestion(error_line, error_type)

        debug_msg = (
            f"Error found:\n{tb_str}\n\n"
            f"Explanation:\n{error_type}: {details['explanation']}\n"
            f"Suggested Fix:\n{details['fix']}\n"
            f"Minimal Patch:\n{patch}"
        )

        if interactive:
            # Enter post-mortem debugging
            pdb.post_mortem()

        return debug_msg
