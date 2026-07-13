from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    sample = {
        'name': 'Jane Doe',
        'title': 'Product Designer',
        'email': 'jane@example.com',
        'phone': '(555) 123-4567',
        'linkedin': 'linkedin.com/in/janedoe',
        'summary': 'Designs delightful user experiences for web and mobile. Skilled in research, prototyping, and visual design.',
        'experiences': [
            {'role': 'Senior Product Designer', 'company': 'Acme Co.', 'dates': '2021–Present', 'details': 'Led redesigned onboarding; improved activation by 30%.'},
            {'role': 'Product Designer', 'company': 'Beta Labs', 'dates': '2018–2021', 'details': 'Built design systems and shipped 10+ features.'}
        ],
        'education': [
            {'degree': 'B.Des, Interaction Design', 'school': 'State University', 'dates': '2014–2018'}
        ],
        'skills': ['Figma', 'User Research', 'Prototyping', 'HTML/CSS']
    }
    return render_template('index.html', sample=sample)


@app.route('/preview', methods=['POST'])
def preview():
    data = request.get_json() or {}
    experiences = data.get('experiences', [])
    education = data.get('education', [])
    skills = data.get('skills', [])
    return render_template('resume.html',
                           name=data.get('name', ''),
                           title=data.get('title', ''),
                           email=data.get('email', ''),
                           phone=data.get('phone', ''),
                           linkedin=data.get('linkedin', ''),
                           summary=data.get('summary', ''),
                           experiences=experiences,
                           education=education,
                           skills=skills)


if __name__ == '__main__':
    app.run(debug=True)
