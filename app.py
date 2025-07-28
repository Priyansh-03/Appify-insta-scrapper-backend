from flask import Flask, request, jsonify
from apify_scraper import scrape_profile
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "✅ Instagram Scraper is working! Use the endpoint /analyze/<username> to fetch data."
    })

@app.route("/analyze/<username>", methods=["GET"])
def analyze(username):
    try:
        profile = scrape_profile(username)
        if not profile:
            return jsonify({"error": "Profile not found or Apify failed"}), 404

        output = {
            "username": username,
            "profile_data": profile
        }

        with open("output.json", "w") as f:
            json.dump(output, f, indent=2)

        return jsonify(output)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
