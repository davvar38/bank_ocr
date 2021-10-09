ROOT_FOLDER=$(realpath $(dir Makefile))
BANK_OCR_PATH=$(ROOT_FOLDER)/bank_ocr

install:
	cd $(BANK_OCR_PATH) && poetry install --no-root

test:
	cd $(BANK_OCR_PATH) && poetry run pytest tests/
