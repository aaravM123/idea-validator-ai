def market_trend_check(idea: str) -> str:
    """
    Analyzes if a startup idea aligns with current market trends.
    
    Args:
        idea (str): The startup idea description
        
    Returns:
        str: Analysis result indicating which trends the idea matches
    """
    trending = ["AI", "sustainability", "remote work", "health", "education"]
    matches = [trend for trend in trending if trend.lower() in idea.lower()]
    return f"The idea matches these hot trends: {', '.join(matches)}" if matches else "No current trend matches found." 