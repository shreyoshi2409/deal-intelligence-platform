
from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

API_KEY = "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"

# -------------------------------
# Feature 5 — Session Memory (global counters)
deal_counter = 0
high_risk_count = 0
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def home():
    global deal_counter, high_risk_count

    # Initialize variables
    email = None
    risk_score = None
    next_action = None
    risk_level = None
    decay_warning = None
    win_probability = None
    explanation_text = ""
    strategy = ""

    if request.method == "POST":
        # -------------------------------
        # Inputs
        deal_name = request.form.get("deal_name")
        deal_value = int(request.form.get("deal_value"))
        last_contact = int(request.form.get("last_contact"))
        sentiment = request.form.get("sentiment")
        notes = request.form.get("notes")
        tone = request.form.get("tone")
        # -------------------------------

        # -------------------------------
        # Prompt for OpenRouter/GPT
        prompt = f"""
        Deal Name: {deal_name}
        Deal Value: {deal_value}
        Last Contact: {last_contact}
        Client Sentiment: {sentiment}
        Notes: {notes}
        Tone: {tone}

        Provide output in EXACT format:

        FOLLOW-UP EMAIL:
        <email content>

        RISK SCORE:
        <number between 0-100>%

        SUGGESTED NEXT ACTION:
        <clear next step>
        """
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        output = result["choices"][0]["message"]["content"]
        # -------------------------------

        # -------------------------------
        # Parse structured output
        try:
            email = re.search(r"FOLLOW-UP EMAIL:\n(.+?)\n\nRISK SCORE:", output, re.DOTALL).group(1).strip()
            risk_score = int(re.search(r"RISK SCORE:\n(\d+)%", output).group(1))
            next_action = re.search(r"SUGGESTED NEXT ACTION:\n(.+)", output, re.DOTALL).group(1).strip()
        except:
            email = output
            risk_score = 50
            next_action = "Review deal manually."
        # -------------------------------

        # -------------------------------
        # Risk level
        if risk_score >= 70:
            risk_level = "high"
        elif risk_score >= 40:
            risk_level = "medium"
        else:
            risk_level = "low"
        # -------------------------------

        # -------------------------------
        # Feature 1 — Deal Decay Detection
        if last_contact > 10 and sentiment in ["neutral", "negative"] and deal_value > 50000:
            decay_warning = "⚠️ This deal is entering a decay phase due to inactivity and weak sentiment."
        # -------------------------------

        # -------------------------------
        # Feature 2 — Win Probability
        win_probability = 100 - risk_score
        # -------------------------------

        # -------------------------------
        # Feature 3 — Explainability
        explanation = []
        if last_contact > 7:
            explanation.append("No recent follow-up activity.")
        if sentiment == "negative":
            explanation.append("Client sentiment is negative.")
        if deal_value > 75000:
            explanation.append("High deal value increases risk sensitivity.")
        explanation_text = " ".join(explanation)
        # -------------------------------

        # -------------------------------
        # Feature 4 — Strategic Recommendation
        strategy = "Maintain standard follow-up cadence."
        if risk_score > 70:
            strategy = "Escalate internally or schedule urgent call."
        elif risk_score > 40:
            strategy = "Send personalized follow-up and offer value reinforcement."
        elif win_probability > 70:
            strategy = "Momentum phase detected. Consider closing conversation."
        # -------------------------------

        # -------------------------------
        # Feature 5 — Session Memory
        deal_counter += 1
        if risk_score > 70:
            high_risk_count += 1
        # -------------------------------

    # -------------------------------
    # Render template
    return render_template(
        "index.html",
        email=email,
        risk_score=risk_score,
        next_action=next_action,
        risk_level=risk_level,
        decay_warning=decay_warning,
        win_probability=win_probability,
        explanation=explanation_text,
        strategy=strategy,
        deal_counter=deal_counter,
        high_risk_count=high_risk_count
    )
    # -------------------------------

if __name__ == "__main__":
    app.run(debug=True)