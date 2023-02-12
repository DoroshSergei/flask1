from flask import Flask, render_template
import json
import utils

app = Flask(__name__)
path = 'candidates.json'


@app.route('/')
def page_list():
    candidates = utils.load_candidates_from_json(path)
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def candidate_page(x):
    candidate = utils.get_candidate(x, path)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name, path)
    quantity_candidates = len(candidates)
    return render_template('search.html', candidates=candidates, quantity_candidates=quantity_candidates)


@app.route('/skill/<skill_name>')
def skill_page(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name, path)
    quantity_candidates = len(candidates)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name, quantity_candidates=quantity_candidates)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
