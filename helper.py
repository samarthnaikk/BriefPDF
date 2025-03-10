import google.generativeai as genai

def response(text):
    genai.configure(api_key="your_key")
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Format the following text in LaTeX **without** \documentclass, \begin{{document}}, or \end{{document}}.
    - Use \\section{{}} and \\subsection{{}} where necessary.
    - Use \\begin{{itemize}} and \\item for key points.
    - If a backslash (\\) is needed, use \\textbackslash{{}}.
    - Ensure readability and structure.
    - Summarize the text

    **Text to format:**
    {text}
    """

    response = model.generate_content(prompt)
    return response.text
