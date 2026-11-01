from automation.open_apps import (
    open_chrome,
    open_youtube,
    open_vscode,
    open_notepad,
    open_calculator,
)

from automation.browser import (
    search_google,
)

from automation.youtube import (
    play_youtube,
)

FUNCTIONS = {
    "open_chrome": open_chrome,
    "open_youtube": open_youtube,
    "open_vscode": open_vscode,
    "open_notepad": open_notepad,
    "open_calculator": open_calculator,
    "google_search": search_google,
    "play_youtube": play_youtube,
}