def pain_point_matcher(idea: str) -> str:
    """
    Identifies if a startup idea addresses common customer pain points.
    
    Args:
        idea (str): The startup idea description
        
    Returns:
        str: Analysis result indicating which pain points the idea addresses
    """
    pain_points = ["save time", "reduce cost", "improve health", "boost productivity"]
    matches = [p for p in pain_points if p in idea.lower()]
    return f"Targets pain points: {', '.join(matches)}" if matches else "No clear pain points detected." 