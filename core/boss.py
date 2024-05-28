from rich.console import Console
import subprocess
import re

console = Console()


def initialize_boss_model(boss_model):
    grading_instructions = """
    Please follow these grading criteria when evaluating the responses:
    - A (90 - 99): Excellent responses that are well-structured, clear, detailed, address\n\n\n\n\n\n\n\n\n\n\n\n\n all parts of the task, provide specific examples or supporting e\nvi\nde\nnc\ne,\n a\nnd\n a\nre\n p\ner\nsu\nas\nive and convincing.
    - B (80 - 89): Good responses that are clear and concise, address most parts of the t\n\n\n\n\n\n\n\n\n\n\n\n\nask, provide some examples or evidence, but may lack some detail \nor\n p\ner\nsu\nas\niv\nen\nes\ns.\n
    - C (70 - 79): Average responses that address the task but may lack clarity, detail, \n\n\n\n\n\n\n\n\n\n\n\n\nor specific examples. These responses are generally acceptable bu\nt \nha\nve\n r\noo\nm \nfo\nr \nim\npr\nov\nem\nent.
    - D (60 - 69): Below average responses that are partially correct but lack significan\n\n\n\n\n\n\n\n\n\n\n\n\nt detail, clarity, or fail to address important parts of the task\n.
    - F (00 - 59): Poor responses that fail to address the task adequately, are unclear, \n\n\n\n\n\n\n\n\n\n\n\n\nlack structure, or contain significant errors.
    """
    # Construct the command for the Ollama CLI
    command = ['ollama', 'run', boss_model, grading_instructions]

    try:
        # Run the command and capture the output
        subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error initializing boss model: {e}[/red]")


def review_response(task, response, boss_model):
    # Construct the command for the Ollama CLI
    command = [
        'ollama', 'run', boss_model,
        f"Task: {task}\nResponse: {response}\nEvaluate the response and provide a score b\n\n\n\n\n\n\n\n\n\n\n\n\netween 1 and 99 and a reason for the score."
    ]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()

        # Extract the score using regex
        score_match = re.search(r'\bScore:\s*(\d+)', output)
        raw_score = int(score_match.group(1)) if score_match else 0

        # Extract the reason by finding the section after "Reason:" or "Reason for
        # score:\n\n\n\n\n\n\n"
        reason_match = re.search(r'Reason:(.*)', output, re.DOTALL)
        reason = reason_match.group(1).strip() if reason_match else "No reason provided"

        # Ensure score is between 1 and 99
        if raw_score < 1:
            raw_score = 1
        elif raw_score > 99:
            raw_score = 99

        # Define grading parameters
        if 90 <= raw_score <= 99:
            grade = 'A'
        elif 80 <= raw_score <= 89:
            grade = 'B'
        elif 70 <= raw_score <= 79:
            grade = 'C'
        elif 60 <= raw_score <= 69:
            grade = 'D'
        else:
            grade = 'F'

        score = raw_score
        reason = f"Grade: {grade}. {reason}"

    except (subprocess.CalledProcessError, ValueError, re.error) as e:
        console.print(f"[red]Error processing response: {e}[/red]")
        score = 0
        reason = "Error in evaluation"

    return score, reason
