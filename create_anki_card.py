import requests
import sys

def add_leetcode_card(name, question, answer, tags=None):
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Leetcode",
                "modelName": "Leetcode",
                "fields": {
                    "Problem Name": name,
                    "Question": question,
                    "Answer": answer,
                },
                "tags": tags or [],
                "options": {
                    "allowDuplicate": False
                }
            }
        }
    }
    answer = answer.replace('\n', '<br>')
    res = requests.post("http://localhost:8765", json=payload).json()
    if res["error"] is None:
        print(f"✅ Card added successfully with note ID {res['result']}")
    else:
        print(f"❌ Error: {res['error']}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python add.py <Problem Name> <Question> <Answer> [<tag1> <tag2> ...]")
        sys.exit(1)

    problem_name = sys.argv[1]
    question = sys.argv[2]
    answer = sys.argv[3]
    tags = sys.argv[4:] if len(sys.argv) > 4 else []

    add_leetcode_card(problem_name, question, answer, tags)

