# Check if numpy is already installed
if (-not (Get-Module -ListAvailable numpy)) {
    Write-Host "Installing requirments..."
    pip install numpy
    # You might need to use Invoke-WebRequest or Invoke-RestMethod to install numpy if pip is not available
}

Write-Host "Do you want to start the programm now: "
Write-Host 'y/n'

$start_or_not = Read-Host "Enter do you want to start the programm nowL Y/N: "

switch ($start_or_not.ToLower()) {
    'y' {
        Set-Location "..\src\"
        try {
            python main.py
        } catch {
            Write-Host "Error starting the program: $_"
            Start-Sleep -Seconds 5
            exit
        }
    }
    'n' {
        Write-Host "We are quitting..."
        Start-Sleep -Seconds 5
        exit
    }
    default {
        Write-Host "Invalid input. Please enter 'y' or 'n'."
        Start-Sleep -Seconds 5
        exit
    }
}