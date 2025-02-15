import re
from typing import List, Tuple

def get_patterns() -> List[Tuple[re.Pattern, str]]:
    """
    Returns a list of compiled regex patterns and corresponding suggestions.
    """
    patterns = [
        # Use 'is None' instead of '== None'
        (re.compile(r'==\s*None'), "Yo, consider using 'is None' instead of '== None' for better clarity."),
        # Recommend using logging over print statements
        (re.compile(r'\bprint\s*\(.*\)'), "Heads up: Logging is usually a smarter choice than print statements in production."),
        # Suggest iterating directly over items
        (re.compile(r'for\s+\w+\s+in\s+range\(len\('), "Tip: Try iterating directly over items instead of using index-based loops."),
        # Flag use of '== True' or '== False'
        (re.compile(r'==\s*(True|False)'), "FYI: Avoid comparing directly to True or False; consider using implicit truthiness."),
        # Warn about TODO comments left in code
        (re.compile(r'#\s*TODO'), "Reminder: Make sure to address any TODO comments before production deployment."),
    ]
    return patterns
