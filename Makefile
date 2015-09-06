
SPHINX_BUILD   = sphinx-build
SPHINX_APIDOC   = sphinx-apidoc

DOC_SDIR = docs
BUILD_DIR = build
SOURCE_DIR = $(BUILD_DIR)/source

SOURCE_FILES = $(shell find torrentfile -type f -name '*.py')
DOC_FILES = $(shell find $(DOC_SDIR) -type f)

.PHONY: apidoc html clean

$(SOURCE_DIR): $(SOURCE_FILES) $(DOC_FILES)
	mkdir --parents "$(SOURCE_DIR)"
	cp --archive "$(DOC_SDIR)/." --target-directory="$(SOURCE_DIR)"

apidoc: $(SOURCE_DIR)
	$(SPHINX_APIDOC) --force --output-dir=$(SOURCE_DIR) torrentfile/

html: clean $(SOURCE_DIR) apidoc
	@# $(SPHINX_BUILD) -b html "$(SOURCE_DIR)" "$(BUILD_DIR)/html"
	$(SPHINX_BUILD) -b dirhtml "$(SOURCE_DIR)" "$(BUILD_DIR)/html"

clean:
	rm -rf $(BUILD_DIR)
