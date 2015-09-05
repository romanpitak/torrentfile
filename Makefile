
SPHINX_BUILD   = sphinx-build
SPHINX_APIDOC   = sphinx-apidoc

DOC_SDIR = docs
BUILD_DIR = build
SOURCE_DIR = $(BUILD_DIR)/source

SOURCE_FILES = $(shell find torrentfile -type f -name '*.py')
DOC_FILES = $(shell find $(DOC_SDIR) -type f)

.PHONY: apidoc html clean

$(SOURCE_DIR): $(SOURCE_FILES) $(DOC_FILES)
	make clean
	mkdir --parents "$(SOURCE_DIR)"
	cp --archive "$(DOC_SDIR)/." --target-directory="$(SOURCE_DIR)"
	make apidoc

apidoc: $(SOURCE_DIR)
	$(SPHINX_APIDOC) --force --output-dir=$(SOURCE_DIR) torrentfile/

html: $(SOURCE_DIR)
	@# $(SPHINX_BUILD) -b html "$(SOURCE_DIR)" "$(BUILD_DIR)/html"
	$(SPHINX_BUILD) -b dirhtml "$(SOURCE_DIR)" "$(BUILD_DIR)/html"

clean:
	rm -rf $(BUILD_DIR)
