from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Are You Free Wednesday?</title>
    <style>
        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #ffe4ec, #f7e8ff, #e8f0ff);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card {
            width: 90%;
            max-width: 500px;
            background: white;
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        h1 {
            color: #333;
        }

        button {
            padding: 12px 20px;
            margin: 10px;
            border: none;
            border-radius: 999px;
            cursor: pointer;
            font-size: 16px;
        }

        .yes-btn {
            background: #ff7eb6;
            color: white;
        }

        .no-btn {
            background: #ddd6f3;
            color: #333;
        }

        textarea {
            width: 100%;
            height: 100px;
            margin-top: 15px;
            padding: 12px;
            border-radius: 12px;
            border: 1px solid #ccc;
            font-size: 15px;
            box-sizing: border-box;
        }

        .submit-btn {
            background: #7c5cff;
            color: white;
            width: 100%;
            margin-top: 15px;
        }

        .response-box {
            margin-top: 20px;
            background: #f9f3ff;
            padding: 15px;
            border-radius: 12px;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hermella wants to know if you're free Wednesday</h1>
        <p>Pick an answer or type a reply.</p>

        <form method="POST">
            <button class="yes-btn" type="submit" name="answer" value="Yes">Yes</button>
            <button class="no-btn" type="submit" name="answer" value="Not free">Not free</button>

            <textarea name="reply" placeholder="Type your reply here"></textarea>
            <button class="submit-btn" type="submit">Send reply</button>
        </form>

        {% if submitted %}
        <div class="response-box">
            <strong>Saved response:</strong><br><br>
            {% if answer %}
                Choice: {{ answer }}<br>
            {% endif %}
            {% if reply %}
                Message: {{ reply }}
            {% endif %}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    reply = ""
    submitted = False

    if request.method == "POST":
        answer = request.form.get("answer", "")
        reply = request.form.get("reply", "")
        submitted = True

    return render_template_string(
        PAGE_HTML,
        answer=answer,
        reply=reply,
        submitted=submitted
    )

if __name__ == "__main__":
    app.run(debug=True)