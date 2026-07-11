@echo off
echo Starting local web server for DKNOTT Website...
echo Please open your browser and go to: http://localhost:8000/templates/wedding-films.html
echo Press Ctrl+C to stop the server.
python -m http.server 8000
pause
