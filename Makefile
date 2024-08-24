# formatting
NONE=\033[00m
RED=\033[01;31m
GREEN=\033[01;32m
YELLOW=\033[01;33m
PURPLE=\033[01;35m
CYAN=\033[01;36m
WHITE=\033[01;37m
BOLD=\033[1m
UNDERLINE=\033[4m


help:
	@echo ""
	@echo "${BOLD}${PURPLE}This repository is to learn more about Data Engineering Projects"
	@echo ""
	@echo "${YELLOW}Please following the setup process in the README.md file. ${NONE}"
	@echo ""
	@echo "${CYAN}Run the any of the following commands: ${NONE}"
	@echo ""
	@echo "${GREEN}run-code : Runs the main.py script ${NONE}"
	@echo ""

run-code:
	@echo "${BOLD}${GREEN}Running the main.py script ${NONE}"
	python src/main.py

#TODO
# 1. How to run the tests
