from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            tasks.append({"title": title, "done": False})
        return redirect("/")
    return render_template("index.html", tasks=tasks)

@app.route("/toggle/<int:i>", methods=["POST"])
def toggle(i):
    if 0 <= i < len(tasks):
        tasks[i]["done"] = not tasks[i]["done"]
    return redirect("/")

@app.route("/delete/<int:i>", methods=["POST"])
def delete(i):
    if 0 <= i < len(tasks):
        tasks.pop(i)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
