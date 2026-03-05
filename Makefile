.PHONY: docs clean-docs

docs:
	pydoctor

clean-docs:
	rm -rf apidocs
