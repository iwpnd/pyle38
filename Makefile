.PHONY: install
install:
	@echo "installing"
	@uv sync
	@uv run pre-commit install
	@uv run pre-commit install --hook-type commit-msg
	@uv run pre-commit install --hook-type prepare-commit-msg
	@echo "install complete"

.PHONY: check
check:
	@echo "check lockfile consistency"
	@uv lock --locked
	@echo "run pre-commit hooks"
	@uv run pre-commit run -a
	@echo "run mypy checks"
	@uv run mypy --ignore-missing-imports --config-file pyproject.toml
	@echo "check for obsolete dependencies"
	@uv run deptry src

.PHONY: test
test:
	@echo "run tests"
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml -vv -s

.PHONY: build
build: clean-build
	@echo "creating wheel"
	@uvx --from build pyproject-build --installer uv

.PHONY: clean-build
clean-build:
	@echo "remove build artifacts"
	@uv run python -c "import shutil; import os; shutil.rmtree('dist') if os.path.exists('dist') else None"

.PHONY: help
help:
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
