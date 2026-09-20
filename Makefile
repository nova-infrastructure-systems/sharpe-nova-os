PYTHON ?= .venv/bin/python

.PHONY: \
	require-venv \
	verify \
	verify-doctrine \
	verify-scenarios \
	verify-gate3-field-derivation \
	verify-target-v2-contract \
	verify-gate5-entry-design \
	verify-public-surface \
	verify-publication-governance \
	verify-identity-protection \
	verify-tests \
	verify-whitespace \
	test

require-venv:
	@test -x "$(PYTHON)" || \
	  (echo "Repository Python not found: $(PYTHON)" >&2; \
	   echo "Run the repository bootstrap command first." >&2; \
	   exit 1)

verify: \
	verify-doctrine \
	verify-scenarios \
	verify-gate3-field-derivation \
	verify-target-v2-contract \
	verify-gate5-entry-design \
	verify-public-surface \
	verify-publication-governance \
	verify-identity-protection \
	verify-tests \
	verify-whitespace

verify-doctrine: require-venv
	$(PYTHON) scripts/doctrine_lint.py



verify-scenarios: require-venv
	$(PYTHON) scripts/run_decision_scenario_suite.py --report /tmp/nova-public-decision-scenario-report.md

verify-gate3-field-derivation: require-venv
	$(PYTHON) scripts/validate_gate3_field_derivation.py

verify-target-v2-contract: require-venv
	$(PYTHON) scripts/validate_target_v2_contract_revision.py

verify-gate5-entry-design: require-venv
	$(PYTHON) scripts/validate_gate5_entry_design_review.py

verify-public-surface: require-venv
	$(PYTHON) scripts/validate_public_surface_coherence.py

verify-publication-governance: require-venv
	$(PYTHON) scripts/validate_publication_governance.py

verify-identity-protection: require-venv
	$(PYTHON) scripts/validate_identity_protection.py

verify-tests: require-venv
	$(PYTHON) -m pytest

verify-whitespace:
	git diff --check

test: verify-tests
