import nimporter
from nimporter import nexporter, nimporter as nm, get_nim_extensions
import setuptools


setuptools.setup(
    name = "isu",
    package_Data={'': ["*.nim*", "*.ui", "*.qrc", "*.png", "*.demo", "*.qml"]},
    # platforms=[sys.platform],
    setup_requires = [
        "choosenim_install"
    ],
    install_requires = [ "nimporter" ]
    # ext_modules=get_nim_extensions(["win32"], "isu"),
)