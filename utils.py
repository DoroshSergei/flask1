import json


def load_candidates_from_json(path):
    return json.load(open(path, encoding='utf-8'))


def get_candidate(candidate_id, path):
    for candidate in load_candidates_from_json(path):
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name, path):
    candidates = []
    for candidate in load_candidates_from_json(path):
        if candidate_name in candidate["name"].split(' ')[0]:
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name, path):
    candidates = []
    for candidate in load_candidates_from_json(path):
        if skill_name in candidate["skills"].lower():
            candidates.append(candidate)
    return candidates








