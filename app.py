from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

items = []

def validate_item(item):
    return item is not None and isinstance(item, str) and len(item.strip()) > 0

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if validate_item(item):
        items.append(item.strip())
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
