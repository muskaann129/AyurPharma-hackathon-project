from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.organization= "org-6TkGAhNERH3oaXZdCOTzfezK"
openai.api_key = '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'

@app.route('/')
def intro():
    return render_template('index.html')
@app.route('/data',methods=["POST"])   
def data():
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    problem = request.form.get("problem")

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Answer me as an Ayurvedic doctor and i'm your patient. Hey I am {name} and I am {age} years old {gender}.  suggest me some Medicines and formulations for {problem} based on the Ayurvedic classical books/Repositories. answer in about 100 words."}
    ]
    )
    response = completion['choices'][0]['message']['content']
    return render_template('chat.html',data={"solve": response})

if __name__ == '__main__':
    app.run(debug=True)