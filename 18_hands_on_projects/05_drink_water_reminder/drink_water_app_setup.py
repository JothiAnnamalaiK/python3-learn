from setuptools import setup

# pip install py2app

# APP = ["drink_water.py"]
# APP = ["drink_water_menu.py"]

APP = ["drink_water_app.py"]

OPTIONS = {
    "argv_emulation": True,
    "iconfile": "drinkwater.ico",  # replace with the actual path to your .icns file
    "plist": {
        "CFBundleName": "DrinkWaterReminder",
        "CFBundleDisplayName": "Drink Water Reminder",
        "CFBundleIdentifier": "com.yourname.drinkwater",
        "CFBundleVersion": "1.0",
        "CFBundleShortVersionString": "1.0",
        "LSUIElement": False,  # for Dock app
        # "LSUIElement": True  # for Menu-bar only app
    },
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)


# riun this with: python drink_water_app_setup.py py2app
# After building, you’ll find your app in:
# dist/drink_water.app


# Delete previous build folders (optional but clean):
# rm -rf build dist


# To debug launch err:
# cd dist/DrinkWaterReminder.app/Contents/MacOs
# Launch from here using    ./DrinkWaterReminder
