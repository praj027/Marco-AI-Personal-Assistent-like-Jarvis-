import json
import subprocess

from automation.open_apps import open_app as legacy_open_app
from automation.browser import search_google, open_website
from automation.youtube import play_youtube


def open_app(app_name):
    """
    Generic Windows application launcher.

    First searches Windows Start Menu applications.
    If that fails, falls back to Marco's existing app launcher.
    """

    if not app_name:
        return False

    name = str(app_name).strip()

    try:
        # Ask Windows for installed Start Menu applications.
        ps_script = r'''
param($Query)

$apps = Get-StartApps |
    Where-Object {
        $_.Name -like "*$Query*" -or
        $_.AppID -like "*$Query*"
    }

if ($apps) {
    $app = $apps | Select-Object -First 1
    Write-Output ($app.Name + "|||" + $app.AppID)
}
'''

        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                ps_script,
                name,
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )

        output = result.stdout.strip()

        if output and "|||" in output:
            app_title, app_id = output.split("|||", 1)

            launch = subprocess.run(
                [
                    "explorer.exe",
                    f"shell:AppsFolder\\{app_id}",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if launch.returncode == 0:
                print(f"🚀 Opened application: {app_title}")
                return True

    except Exception as error:
        print(f"⚠️ Generic app launcher failed: {error}")

    # Preserve existing Marco functionality.
    try:
        result = legacy_open_app(name)

        if result is False:
            return False

        print(f"🚀 Existing launcher used: {name}")
        return True

    except Exception as error:
        print(f"❌ Existing app launcher failed: {error}")
        return False


TOOLS = {

    "open_app": {
        "function": open_app,
        "description": (
            "Open any application installed on the Windows computer. "
            "Use the actual application name supplied by the user."
        )
    },

    "open_website": {
        "function": open_website,
        "description": "Open any website."
    },

    "google_search": {
        "function": search_google,
        "description": "Search anything on Google."
    },

    "play_youtube": {
        "function": play_youtube,
        "description": "Play anything on YouTube."
    }

}
