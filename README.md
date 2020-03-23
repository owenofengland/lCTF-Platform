# lCTF - CTF Platform designed to teach CTF and Security!

## To Do
* Routes, and templates for challenges
* Flag generation/regeneration
* Deployment logistics
* Autoescape for XSS protection in Jinja Templates

### Some Important Notes

* If the Database seems broken run `db_reset.sh`
* The color scheme is in `ctf/static/color-refs.json`
* `serve.sh` is for deployment, `test.sh` is for testing
* Be sure to pip freeze to requirements.txt on every commit
* Update .gitignore and README.md frequently
* Reset (look into migration integration) DB on adding new challenges