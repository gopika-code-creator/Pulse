# Pulse - Daily Summary Bot

## Overview

Pulse is a Python automation bot that generates a daily summary containing weather information and a motivational quote. The bot runs automatically using GitHub Actions and saves the output as a downloadable artifact.

## Features

* Fetches current weather information
* Retrieves a motivational quote
* Generates a daily summary report
* Runs automatically on a schedule
* Stores the generated summary as a GitHub Actions artifact

## Tech Stack

* Python 3.11
* Requests
* GitHub Actions
* YAML

## Project Structure

```text
Pulse/
├── bot.py
├── requirements.txt
└── .github/
    └── workflows/
        └── daily.yml
```

## Installation

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the bot locally:

```bash
python bot.py
```

## Automation

The bot is configured with GitHub Actions and can be triggered:

* Automatically on a schedule
* Manually using the "Run workflow" button in the Actions tab

## Output

The workflow generates:

* `daily_summary.txt`

This file is uploaded as a GitHub Actions artifact named `daily-summary`.

## Learning Outcomes

This project demonstrates:

* Python scripting
* API consumption
* Error handling
* Git and GitHub workflows
* GitHub Actions automation
* Basic DevOps concepts

```
```
