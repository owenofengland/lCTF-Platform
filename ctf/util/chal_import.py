from json import load
from os.path import exists, isfile
from sys import exit, path
from ctf.models.Challenge import Challenge
from ctf.models.Category import Category
from ctf import db
path.append(".")


def bad_import_print():
    print("Bad Import")
    print("Verify imports folder exists, and that challenges.json exists within imports.")
    print("Follow the example of the one in the GitHub repository or the application will not work or break!")


def exists_and_is_json(fp):
    return exists(fp) and isfile(fp)


def get_import():
    if exists_and_is_json("ctf/import/challenges.json"):
        try:
            challengeFP = open("ctf/import/challenges.json", "r")
            return load(challengeFP)
        except Exception as e:
            bad_import_print()
            print(e)
            exit()
    else:
        bad_import_print()
        exit()


def add_categories_to_db(categories):
    print("[*] Adding categories to the database")
    for category in categories:
        try:
            new_category = Category(name=category)
            db.session.add(new_category)
            db.session.commit()
            print("[*] Added category %s to the database" % category)
        except Exception as e:
            print("[!] Failed to add %s to the database" % category)
            print(e)


def add_challenges_to_db(challenges):
    print("[*] Adding challenges to the database")
    for challenge in challenges:
        name = challenge["name"]
        value = challenge["value"]
        solves = challenge["solves"]
        desc = challenge["desc"]
        flag = challenge["flag"]
        category_id = challenge["category"]

        try:
            new_challenge = Challenge(
                name=name, value=value, solves=solves, desc=desc, flag=flag, category_id=category_id)
            db.session.add(new_challenge)
            db.session.commit()
            print("[*] Added challenge %s to the database" % name)
        except Exception as e:
            print("[!] Failed to add %s to the database" % name)
            print(e)


def add_to_db():
    challengeData = get_import()
    categories, challenges = challengeData["categories"], challengeData["challenges"]
    add_categories_to_db(categories)
    print("[*] Categories finished")
    add_challenges_to_db(challenges)
    print("[*] Challenges finished")
    print("[*] Done")
