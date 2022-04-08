
SOURCES_DIR = caresse
TESTS_DIR   = tests


help:  #help:Show this help.
	@echo 'Usage:'
	@echo '  make [target] ...'
	@echo 

	@echo 'Examples:'
	@echo '  make help'
	@echo '  make all'
	@echo 

	@echo 'Available targets:'
	@egrep "#help:" $(MAKEFILE_LIST) | grep -v egrep | perl -pe 's|^(.+?):.+#help:(.*)$$|\1\t\2|' | awk -F "\t" '{printf "  %-25s%s\n", $$1, $$2}'
	@echo 

	@echo 'Available variables:'
	@echo '  SOURCES_DIR, TESTS_DIR, version'
	@echo 


all: setup-hooks sort-imports format lint test test-train #help:Run the quality pipeline locally: sort-import, format, lint-quick

# setup project hooks
_setup-check:
	@python -c "import black"
	@python -c "import isort"
	@python -c "import flake8"
	@python -c "import pylint"
	@python -c "import bandit"

_setup-on-error:
	@echo "-- You may want to run:"
	@echo "    \`pip install -U isort black bandit flake8 flake8_quotes pylint pytest pytest-cov pytest-xdist pytest-rerunfailures pytest-custom_exit_code\`"

_setup:
	@($(MAKE) --no-print-directory _setup-check || $(MAKE) --no-print-directory _setup-on-error)

setup-hooks: .git | _setup  #help:Setup hooks in the current git repository.
	@echo "-- Setting up Git hooks"
	chmod +x hooks/pre-commit
	ln -fs $(abspath scripts/pre-commit) .git/hooks/pre-commit
	chmod +x hooks/pre-push
	ln -fs $(abspath scripts/pre-push) .git/hooks/pre-push


# apply format
sort-imports: $(SOURCES_DIR) $(TESTS_DIR) | _setup  #help:Sort import
	@echo "-- Sorting imports"
	isort --multi-line VERTICAL_HANGING_INDENT --line-length=120 --tc $^

format: $(SOURCES_DIR) $(TESTS_DIR) | sort-imports  #help:Format code
	@echo "-- Formatting"
	black --line-length=120 $^


# lint
_lint-flake8: $(SOURCES_DIR) $(TESTS_DIR) | _setup
	@echo "-- Linting with flake8"
	flake8 --max-line-length=120 --inline-quotes double  --extend-ignore=E203 $^

_lint-pylint-soft: $(SOURCES_DIR) $(TESTS_DIR) | _setup
	@echo "-- Linting with pylint"
	pylint --max-line-length 120 --extension-pkg-allow-list=pydantic --disable=W,R,C $^

_lint-pylint-hard: $(SOURCES_DIR) $(TESTS_DIR) | _setup
	@echo "-- Linting with pylint"
	pylint --max-line-length 120 --extension-pkg-allow-list=pydantic $^

lint-soft: _lint-flake8 _lint-pylint-soft

lint-hard: _lint-flake8 _lint-pylint-hard

lint-quick: _lint-flake8  #help:Quick lint

lint: lint-soft  #help:Lint the code with soft parameters


# security analysis
security-soft: $(SOURCES_DIR) $(TESTS_DIR)
	@echo "-- Security analysis with bandit"
	bandit --quiet --severity-level medium --confidence-level high -r $^

security-hard: $(SOURCES_DIR) $(TESTS_DIR)
	@echo "-- Security analysis with bandit"
	bandit --quiet -r $^

security: security-soft  #help:Run a security analysis with soft parameters


# run tests
test: $(TESTS_DIR)  #help:Run (unit) tests
	@echo "-- Testing with pytest $(ARGS)"
	pytest --showlocals $<
