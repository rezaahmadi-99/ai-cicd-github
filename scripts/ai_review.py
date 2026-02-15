from google import genai
import sys


client = genai.Client()

def review_code(diff_text):

    """Send a code diff to Gemini for review."""

    prompt = f"""You are an expert code reviewer. Review the following code diff and provide feedback.

                Focus on:
                1. Security vulnerabilities
                2. Bug risks
                3. Performance issues
                4. Best practice violations

                For each issue found, provide:
                - Severity: HIGH / MEDIUM / LOW
                - Description of the issue
                - Suggested fix

                If the code looks good, say so.

                Code diff to review:

                {diff_text}"""


    response = client.models.generate_content(
        model = "gemini-3-flash-preview", contents=prompt
    )

    return response.text


if __name__ == "__main__":
    # if a parameter is passed for the script
    if len(sys.argv) > 1:
        diff_file = sys.argv[1]
        with open(diff_file, 'r') as file:
            diff_content = file.read()

    # if a parameter is not passed for the script
    else:
        diff_content = sys.stdin.read()
    
    # give it to the gemini
    review = review_code(diff_content)
    print(review)