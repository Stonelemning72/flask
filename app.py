from flask import Flask, request, render_template_string

app = Flask(__name__)

word_limit = 200

html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Essay/Letter Checker</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; }
        .container { max-width: 600px; margin: auto; }
        textarea { width: 100%; height: 150px; }
        .results, .marks { margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Topic of Essay/Letter:</h2>
        <form action="/" method="post">
            <input type="text" name="topic" style="width: 100%;" required><br><br>
            <h2>Write your Essay/Letter (Word Limit: 200):</h2>
            <textarea name="essay" required></textarea><br><br>
            <input type="submit" value="Submit">
        </form>
        {% if results %}
            <div class="results">
                <h3>Issues and Suggestions:</h3>
                <p>{{ results }}</p>
            </div>
        {% endif %}
        {% if marks is not None %}
            <div class="marks">
                <h3>Marks: {{ marks }}/100</h3>
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    marks = None

    if request.method == 'POST':
        essay_content = request.form['essay']
        words = essay_content.split()
        if len(words) > word_limit:
            results = f"Word limit of {word_limit} exceeded. Please reduce the word count."
        else:
            # Dummy processing logic
            issues = ["Issue 1: Spelling mistake in 'example'.", "Issue 2: Use of informal language."]
            suggestions = ["Suggestion 1: Replace 'example' with 'sample'.", "Suggestion 2: Use formal language."]
            marks = 75
            results = "Issues:\n" + "\n".join(issues) + "\n\nSuggestions:\n" + "\n".join(suggestions)

    return render_template_string(html_template, results=results, marks=marks)

if __name__ == "__main__":
    app.run(debug=True)
