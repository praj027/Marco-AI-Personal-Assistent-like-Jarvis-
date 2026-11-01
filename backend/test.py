from automation.open_apps import open_chrome

print("MARCO AI TEST STARTED")

if open_chrome():
    print("✅ Chrome opened successfully!")
else:
    print("❌ Chrome could not be opened.")