import nox

locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "tests"

@nox.session(python="3.11")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.11", "3.12"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python=["3.11", "3.12"])
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
