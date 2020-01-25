SDKCONFIG += boards/sdkconfig.pystepper
USER_C_MODULES=../../../firmware/micropython_cmodule
MICROPY_PY_BLUETOOTH = 0
FROZEN_MANIFEST = $(BOARD_DIR)/manifest.py
FROZEN_MPY_DIR = 