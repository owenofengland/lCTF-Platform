from json import load
from os.path import exists, isfile
from sys import exit, path
from ctf.util.flag_generator import generate_flag_buffer
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
        check = Category.query.filter_by(name=category).first()
        if check:
            print("[!] Category %s already in the database" % category)
        else:
            try:
                new_category = Category(name=category)
                db.session.add(new_category)
                db.session.commit()
                print("[*] Added category %s to the database" % category)
            except Exception as e:
                print("[x] Failed to add %s to the database" % category)
                print(e)


def add_challenges_to_db(challenges):
    print("[*] Adding challenges to the database")
    for challenge in challenges:
        name = challenge["name"]
        value = challenge["value"]
        requirement = challenge["requirement"]
        solves = challenge["solves"]
        desc = challenge["desc"]
        link = challenge["link"]
        base_flag = challenge["flag"]
        cur_flag = generate_flag_buffer(base_flag)
        category_id = challenge["category"]

        check = Challenge.query.filter_by(name=name).first()
        if check:
            print("[!] Challenge by name of %s already in the database" % name)
        else:
            try:
                new_challenge = Challenge(
                    name=name, value=value, requirement=requirement, solves=solves, desc=desc, link=link, base_flag=base_flag, cur_flag=cur_flag, category_id=category_id)
                db.session.add(new_challenge)
                db.session.commit()
                print("[*] Added challenge %s to the database" % name)
            except Exception as e:
                print("[x] Failed to add %s to the database" % name)
                print(e)


def add_to_db():
    challengeData = get_import()
    categories, challenges = challengeData["categories"], challengeData["challenges"]
    add_categories_to_db(categories)
    print("[*] Categories finished")
    add_challenges_to_db(challenges)
    print("[*] Challenges finished")
    print("[*] Done")
