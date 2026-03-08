import streamlit as st
import re

st.set_page_config(page_title="AI Code Review Playground", layout="centered")

st.title("AI Code Review Playground")
st.caption("AI-powered pre-review assistant for developers")

st.divider()

language = st.selectbox(
    "Select Programming Language",
    ["Auto Detect", "Swift", "Python", "JavaScript", "Other"]
)

code_input = st.text_area(
    "Paste your code snippet",
    height=300,
    placeholder="Paste your code here..."
)

if code_input:
    st.subheader("Code Preview")
    preview_lang = language.lower() if language != "Auto Detect" else None
    st.code(code_input, language=preview_lang)


def detect_language(code):
    if "func " in code and "URLSession" in code:
        return "Swift"
    if "def " in code and ":" in code:
        return "Python"
    if "function " in code or "=>" in code:
        return "JavaScript"
    return "Other"


def generate_improvement(issue_type, snippet):

    if issue_type == "force_unwrap":
        return f"Detected potentially unsafe expression `{snippet}`. Consider validating the value before usage."

    if issue_type == "silent_error":
        return f"Error handling pattern `{snippet}` may suppress failures. Consider exposing the error to the caller."

    if issue_type == "network_call":
        return f"Network call `{snippet}` detected. Ensure response validation and error handling before processing results."

    if issue_type == "long_function":
        return "This function appears relatively long. Consider splitting responsibilities into smaller reusable functions."

    if issue_type == "missing_comments":
        return "Complex logic detected without inline documentation. Adding comments could improve maintainability."

    return "Consider improving readability and structure for easier maintenance."


def analyze_code(code):

    improvements = []

    force_unwrap_matches = re.findall(r'\w+!\b', code)
    for match in force_unwrap_matches:
        improvements.append(generate_improvement("force_unwrap", match))

    silent_error_matches = re.findall(r'try\?|except:', code)
    for match in silent_error_matches:
        improvements.append(generate_improvement("silent_error", match))

    network_matches = re.findall(r'dataTask|fetch\(', code)
    for match in network_matches:
        improvements.append(generate_improvement("network_call", match))

    if code.count("\n") > 15:
        improvements.append(generate_improvement("long_function", ""))

    if "//" not in code and "#" not in code:
        improvements.append(generate_improvement("missing_comments", ""))

    if len(improvements) == 0:
        improvements.append(generate_improvement("general", ""))

    return improvements[:3]


def generate_positive_note(code):

    if "completion" in code or "callback" in code:
        return "Asynchronous execution patterns are used, which is suitable for non-blocking operations."

    if "try" in code or "catch" in code:
        return "Structured error handling logic is present in the snippet."

    if "func" in code or "def" in code:
        return "The function structure is clearly defined."

    return "The snippet has a straightforward and readable structure."


if st.button("Review Code"):

    if code_input.strip() == "":
        st.warning("Please paste a code snippet.")
    else:

        detected_language = detect_language(code_input) if language == "Auto Detect" else language

        improvements = analyze_code(code_input)
        positive_note = generate_positive_note(code_input)

        st.divider()

        st.subheader("Review Results")
        st.write(f"Detected Language: **{detected_language}**")

        st.markdown("### Improvements")

        for i, improvement in enumerate(improvements, 1):
            st.write(f"{i}. {improvement}")

        st.markdown("### Positive Note")
        st.success(positive_note)

st.divider()
st.caption("Prototype created for AI-assisted code review experimentation by Awais Shahid.")
